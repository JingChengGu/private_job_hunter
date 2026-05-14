"""
matcher.py — Uses Claude API to score each job against Jason's profile

Returns a structured assessment per job:
{
    "score":          int (1–10),
    "should_apply":   bool,
    "match_reasons":  list[str],   # 3 bullet points explaining fit
    "resume_variant": str,         # key from config.RESUME_VARIANTS
    "concern":        str,         # main risk / gap (brief)
}
"""

import json
import logging
import re

import anthropic

from config import JASON_PROFILE, RESUME_VARIANTS

log = logging.getLogger(__name__)

client = anthropic.Anthropic()      # reads ANTHROPIC_API_KEY from env


SYSTEM_PROMPT = f"""You are a job match evaluator for a specific candidate.
Your job is to score how well each job posting matches the candidate's profile
and identify which resume variant to use.

{JASON_PROFILE}

RESUME VARIANTS AVAILABLE:
- biz_ops:       Business Operations Analyst (Qualcomm-style ops roles)
- eng_ops:       Engineering Operations Analyst (BI + coordination + ops)
- data_science:  Data Scientist / Finance & Accounting Automation
- ai_solutions:  AI Solutions / Data Analytics Senior Analyst (Salesforce-style)
- data_analyst:  Data Analyst (Disney-style consumer data / validation)

SCORING RUBRIC:
10 — Perfect match: role type, skills, level, location all align
8–9 — Strong match: core skills align, minor gaps (experience years, location)
6–7 — Reasonable match: worth applying, some tailoring needed
4–5 — Stretch: possible but significant gaps
1–3 — Poor fit: wrong domain, too senior, or missing core requirements

ALWAYS return valid JSON only. No preamble, no markdown, no explanation outside the JSON.
"""

USER_TEMPLATE = """Score this job for the candidate:

COMPANY: {company}
TITLE: {title}
LOCATION: {location}
POSTED: {posted_date}
DESCRIPTION:
{description}

Return ONLY this JSON object:
{{
  "score": <1-10 integer>,
  "should_apply": <true|false>,
  "match_reasons": [
    "<specific reason 1 tied to candidate's actual experience>",
    "<specific reason 2>",
    "<specific reason 3>"
  ],
  "resume_variant": "<one of: biz_ops | eng_ops | data_science | ai_solutions | data_analyst>",
  "concern": "<main gap or risk in one sentence, or 'None' if clean match>"
}}"""


def score_job(job: dict) -> dict:
    """
    Call Claude API to score a single job.
    Returns scoring dict or None on failure.
    """
    description = job.get("description", "")
    if len(description) < 50:
        description = f"Job title: {job['title']} at {job['company']}. Location: {job.get('location', '')}."

    prompt = USER_TEMPLATE.format(
        company=job["company"],
        title=job["title"],
        location=job.get("location", "Not specified"),
        posted_date=job.get("posted_date", "Unknown"),
        description=description[:3500],
    )

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=512,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = message.content[0].text.strip()

        # Strip any accidental markdown fences
        raw = re.sub(r"^```json\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        result = json.loads(raw)

        # Validate required keys exist
        assert "score" in result and "match_reasons" in result and "resume_variant" in result

        # Map to valid variant key
        if result["resume_variant"] not in RESUME_VARIANTS:
            result["resume_variant"] = "biz_ops"   # sensible default

        return result

    except json.JSONDecodeError as e:
        log.error("JSON parse failed for job '%s': %s | Raw: %s", job["title"], e, raw[:200])
        return None
    except Exception as e:
        log.error("Claude API error for job '%s': %s", job["title"], e)
        return None


def score_jobs_batch(jobs: list[dict], min_score: int = 6) -> list[dict]:
    """
    Score a list of jobs. Attaches score data directly to each job dict.
    Returns only jobs that meet min_score threshold.
    """
    scored = []
    for job in jobs:
        log.info("Scoring: %s @ %s ...", job["title"], job["company"])
        result = score_job(job)
        if result is None:
            continue

        job["score"]          = result["score"]
        job["should_apply"]   = result.get("should_apply", result["score"] >= min_score)
        job["match_reasons"]  = result.get("match_reasons", [])
        job["resume_variant"] = result.get("resume_variant", "biz_ops")
        job["concern"]        = result.get("concern", "")

        if job["score"] >= min_score:
            scored.append(job)

    return sorted(scored, key=lambda x: x["score"], reverse=True)
