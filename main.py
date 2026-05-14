"""
main.py — Job Hunter Orchestrator
Run this daily (via GitHub Actions cron) or manually anytime.

Usage:
    python main.py                  # Full run, sends email
    python main.py --dry-run        # Print results, no email
    python main.py --company qualcomm  # Test single company
"""

import argparse
import logging
import os
import re
import sys
from datetime import datetime, timedelta, timezone

import database as db
import scrapers
from config import (
    TARGET_COMPANIES,
    SEARCH_KEYWORDS,
    TITLE_INCLUDE_KEYWORDS,
    TITLE_EXCLUDE_KEYWORDS,
    MIN_MATCH_SCORE,
    MAX_YOE_REQUIRED,
    LOOKBACK_DAYS,
)
from emailer import send_email
from matcher import score_jobs_batch

# ── Logging setup ─────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%Y-%m-%d %H:%M",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("job_hunter.log", encoding="utf-8"),
    ],
)
log = logging.getLogger(__name__)


# ── Filtering helpers ─────────────────────────────────────────────────────────

def _title_passes(title: str) -> bool:
    """True if title matches at least one include keyword and no exclude keywords."""
    t = title.lower()
    if not any(kw in t for kw in TITLE_INCLUDE_KEYWORDS):
        return False
    if any(kw in t for kw in TITLE_EXCLUDE_KEYWORDS):
        return False
    return True


def _too_senior(description: str) -> bool:
    """Rough heuristic: reject if description explicitly requires 5+ years."""
    patterns = [
        r"\b([5-9]|1[0-9])\+?\s*years?\s*of\s*(experience|exp\b)",
        r"\b(5|6|7|8|9|10)\+\s*years?",
        r"minimum\s*(5|6|7|8|9|10)\s*years?",
    ]
    desc_lower = description.lower()
    for pat in patterns:
        if re.search(pat, desc_lower):
            return True
    return False


def _is_recent(posted_date: str, posted_on_raw: str = "") -> bool:
    """
    True if posted within LOOKBACK_DAYS.
    Handles:
      - YYYY-MM-DD date strings
      - Workday relative strings like "Posted 3 Days Ago"
      - Empty string (assume recent, let Claude scoring handle relevance)
    """
    if not posted_date and not posted_on_raw:
        return True     # unknown date → include, score will de-prioritize

    # Parse Workday relative string
    if posted_on_raw:
        raw = posted_on_raw.lower()
        if "today" in raw or "just posted" in raw:
            return True
        m = re.search(r"(\d+)\s*day", raw)
        if m and int(m.group(1)) <= LOOKBACK_DAYS:
            return True
        m = re.search(r"(\d+)\s*week", raw)
        if m and int(m.group(1)) == 1 and LOOKBACK_DAYS >= 7:
            return True
        if "month" in raw:
            return False    # definitely too old
        return True         # ambiguous → include

    # Parse ISO date
    try:
        job_dt = datetime.strptime(posted_date[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
        cutoff = datetime.now(tz=timezone.utc) - timedelta(days=LOOKBACK_DAYS)
        return job_dt >= cutoff
    except ValueError:
        return True


# ── Fetch from all sources ────────────────────────────────────────────────────

def fetch_all(company_filter: str = "") -> list[dict]:
    all_jobs: list[dict] = []

    # — Greenhouse —
    for co in TARGET_COMPANIES.get("greenhouse", []):
        if company_filter and company_filter.lower() not in co["name"].lower():
            continue
        log.info("Fetching Greenhouse: %s", co["name"])
        jobs = scrapers.fetch_greenhouse(co["slug"], co["name"])
        log.info("  → %d jobs returned", len(jobs))
        all_jobs.extend(jobs)

    # — Lever —
    for co in TARGET_COMPANIES.get("lever", []):
        if company_filter and company_filter.lower() not in co["name"].lower():
            continue
        log.info("Fetching Lever: %s", co["name"])
        jobs = scrapers.fetch_lever(co["slug"], co["name"])
        log.info("  → %d jobs returned", len(jobs))
        all_jobs.extend(jobs)

    # — Workday —
    for co in TARGET_COMPANIES.get("workday", []):
        if company_filter and company_filter.lower() not in co["name"].lower():
            continue
        log.info("Fetching Workday: %s", co["name"])
        jobs = scrapers.fetch_workday(
            subdomain=co["subdomain"],
            site_num=co["site_num"],
            tenant=co["tenant"],
            company_name=co["name"],
            keywords=SEARCH_KEYWORDS[:4],   # top 4 keywords per company
        )
        log.info("  → %d jobs returned", len(jobs))
        all_jobs.extend(jobs)

    log.info("Total fetched: %d", len(all_jobs))
    return all_jobs


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run(dry_run: bool = False, company_filter: str = ""):
    db.init_db()
    errors = []

    # 1. Fetch
    log.info("=" * 60)
    log.info("Job Hunter starting — %s", datetime.now().strftime("%Y-%m-%d %H:%M"))
    all_jobs = fetch_all(company_filter)
    total_fetched = len(all_jobs)

    # 2. Filter: dedup, title, recency, seniority
    candidates = []
    for job in all_jobs:
        if db.is_seen(job["id"]):
            continue
        if not _title_passes(job["title"]):
            continue
        if not _is_recent(job.get("posted_date", ""), job.get("posted_on_raw", "")):
            log.debug("Too old, skipping: %s @ %s", job["title"], job["company"])
            continue
        if _too_senior(job.get("description", "")):
            log.debug("Too senior, skipping: %s @ %s", job["title"], job["company"])
            continue
        candidates.append(job)

    log.info("Candidates after filter: %d / %d", len(candidates), total_fetched)

    if not candidates:
        log.info("No new candidates. Nothing to email.")
        db.log_run(total_fetched, 0, 0)
        return

    # 3. Score with Claude API
    log.info("Scoring %d candidates with Claude API...", len(candidates))
    scored = score_jobs_batch(candidates, min_score=MIN_MATCH_SCORE)
    log.info("Matches at %d+: %d", MIN_MATCH_SCORE, len(scored))

    # 4. Save all scored (above threshold) to DB
    for job in scored:
        db.save_job(job)

    # 5. Send email
    if scored:
        log.info("Sending email digest (%d jobs)...", len(scored))
        sent = send_email(scored, dry_run=dry_run)
        if not sent:
            errors.append("Email failed to send")
    else:
        log.info("No matches above threshold — no email sent.")

    db.log_run(total_fetched, len(candidates), len(scored), "; ".join(errors))
    log.info("Run complete.")


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Job Hunter — daily job search automation")
    parser.add_argument("--dry-run",  action="store_true", help="Print results, don't send email")
    parser.add_argument("--company",  type=str, default="",  help="Test a single company by name")
    args = parser.parse_args()

    run(dry_run=args.dry_run, company_filter=args.company)
