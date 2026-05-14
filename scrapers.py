"""
scrapers.py — Job fetching from Greenhouse, Lever, and Workday

All scrapers return a list of normalized Job dicts:
{
    "id":          str   — unique identifier (company_slug + platform_id)
    "company":     str   — company name
    "title":       str   — job title
    "location":    str   — location string
    "url":         str   — direct application URL
    "salary":      str   — salary string if available, else ""
    "posted_date": str   — YYYY-MM-DD if available, else ""
    "description": str   — plain-text job description (for Claude scoring)
}
"""

import requests
import re
import time
import logging
from datetime import datetime, timezone
from bs4 import BeautifulSoup

log = logging.getLogger(__name__)

# ── Shared request config ─────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
}
TIMEOUT = 20


def _clean_html(html_str: str) -> str:
    """Strip HTML tags, collapse whitespace."""
    if not html_str:
        return ""
    text = BeautifulSoup(html_str, "html.parser").get_text(separator=" ")
    return re.sub(r"\s+", " ", text).strip()


def _ts_to_date(ts_ms) -> str:
    """Convert millisecond timestamp to YYYY-MM-DD string."""
    try:
        return datetime.fromtimestamp(int(ts_ms) / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return ""


# ══════════════════════════════════════════════════════════════════════════════
# GREENHOUSE
# ══════════════════════════════════════════════════════════════════════════════

def fetch_greenhouse(company_slug: str, company_name: str) -> list[dict]:
    """
    Public Greenhouse API — no auth needed.
    Returns up to 500 jobs per company.
    """
    url = f"https://boards-api.greenhouse.io/v1/boards/{company_slug}/jobs"
    try:
        resp = requests.get(url, params={"content": "true"}, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        log.warning("Greenhouse fetch failed for %s: %s", company_slug, e)
        return []

    jobs = []
    for j in data.get("jobs", []):
        posted_raw = j.get("updated_at") or j.get("first_published") or ""
        posted_date = ""
        if posted_raw:
            try:
                posted_date = posted_raw[:10]   # "2026-05-13T..."
            except Exception:
                pass

        desc_html = j.get("content", "") or ""
        location_parts = [loc.get("name", "") for loc in j.get("offices", [])]
        location = ", ".join(filter(None, location_parts)) or j.get("location", {}).get("name", "")

        jobs.append({
            "id":          f"gh_{company_slug}_{j['id']}",
            "company":     company_name,
            "title":       j.get("title", ""),
            "location":    location,
            "url":         j.get("absolute_url", ""),
            "salary":      "",
            "posted_date": posted_date,
            "description": _clean_html(desc_html)[:4000],
        })
    return jobs


# ══════════════════════════════════════════════════════════════════════════════
# LEVER
# ══════════════════════════════════════════════════════════════════════════════

def fetch_lever(company_slug: str, company_name: str) -> list[dict]:
    """
    Public Lever API — no auth needed.
    Returns all active postings.
    """
    url = f"https://api.lever.co/v0/postings/{company_slug}?mode=json&limit=250"
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        postings = resp.json()
    except Exception as e:
        log.warning("Lever fetch failed for %s: %s", company_slug, e)
        return []

    jobs = []
    for p in postings:
        created_ms = p.get("createdAt", 0)
        posted_date = _ts_to_date(created_ms)

        # Lever description is split across lists
        desc_parts = []
        for section in p.get("lists", []):
            desc_parts.append(section.get("text", ""))
            for item in section.get("content", "").split("<li>"):
                desc_parts.append(_clean_html(item))
        desc_parts.append(_clean_html(p.get("descriptionPlain", "")))
        description = " ".join(filter(None, desc_parts))[:4000]

        categories = p.get("categories", {})
        location = categories.get("location") or categories.get("commitment") or ""

        apply_url = p.get("applyUrl") or p.get("hostedUrl") or ""

        jobs.append({
            "id":          f"lv_{company_slug}_{p['id']}",
            "company":     company_name,
            "title":       p.get("text", ""),
            "location":    location,
            "url":         apply_url,
            "salary":      "",
            "posted_date": posted_date,
            "description": description,
        })
    return jobs


# ══════════════════════════════════════════════════════════════════════════════
# WORKDAY
# ══════════════════════════════════════════════════════════════════════════════

def _workday_search(subdomain: str, site_num: str, tenant: str, keyword: str) -> list[dict]:
    """
    Hit the Workday CXS API for a single keyword.
    Returns raw jobPostings list.
    """
    url = (
        f"https://{subdomain}.wd{site_num}.myworkdayjobs.com"
        f"/wday/cxs/{subdomain}/{tenant}/jobs"
    )
    payload = {
        "limit": 20,
        "offset": 0,
        "searchText": keyword,
        "appliedFacets": {},
    }
    headers = {**HEADERS, "Content-Type": "application/json"}
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=TIMEOUT)
        resp.raise_for_status()
        return resp.json().get("jobPostings", [])
    except Exception as e:
        log.warning("Workday search failed (%s / %s / '%s'): %s", subdomain, tenant, keyword, e)
        return []


def fetch_workday(subdomain: str, site_num: str, tenant: str,
                  company_name: str, keywords: list[str]) -> list[dict]:
    """
    Search Workday for multiple keywords, deduplicate by job ID.
    Returns normalized job list.
    """
    seen_ids: set[str] = set()
    jobs: list[dict] = []

    for kw in keywords[:6]:          # cap at 6 keywords per company to avoid hammering
        raw = _workday_search(subdomain, site_num, tenant, kw)
        time.sleep(0.5)             # polite delay

        for r in raw:
            wday_id = r.get("bulletFields", [None])[0] or r.get("externalPath", "") or r.get("title", "")
            uid = f"wd_{subdomain}_{wday_id}"
            if uid in seen_ids:
                continue
            seen_ids.add(uid)

            # Build apply URL from externalPath
            ext_path = r.get("externalPath", "")
            apply_url = (
                f"https://{subdomain}.wd{site_num}.myworkdayjobs.com"
                f"/en-US/{tenant}{ext_path}"
            ) if ext_path else ""

            # Workday doesn't return description in search results — note that
            posted_raw = r.get("postedOn", "")
            posted_date = ""
            if "Posted" in posted_raw:          # e.g. "Posted 2 Days Ago"
                posted_date = ""                # relative — main.py uses days filter
            elif posted_raw:
                posted_date = posted_raw[:10]

            jobs.append({
                "id":          uid,
                "company":     company_name,
                "title":       r.get("title", ""),
                "location":    r.get("locationsText", "") or r.get("primaryLocation", ""),
                "url":         apply_url,
                "salary":      r.get("jobReqId", ""),   # sometimes salary is here
                "posted_date": posted_date,
                "posted_on_raw": posted_raw,
                "description": r.get("jobDescription", ""),  # often empty in search
            })

    return jobs
