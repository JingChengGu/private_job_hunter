"""
matcher.py — Rule-based job scorer (no API required, zero cost)
Fixed: location filter, senior title rejection, score calibration, dedup
"""

import logging

log = logging.getLogger(__name__)

# ── US locations — must match at least one ────────────────────────────────────
US_STATES = [
    "california", "ca", "new york", "ny", "texas", "tx", "washington", "wa",
    "illinois", "il", "massachusetts", "ma", "colorado", "co", "georgia", "ga",
    "florida", "fl", "oregon", "or", "nevada", "nv", "arizona", "az",
    "north carolina", "nc", "virginia", "va", "michigan", "mi", "ohio", "oh",
    "san diego", "san francisco", "los angeles", "seattle", "austin", "boston",
    "chicago", "denver", "atlanta", "miami", "new york city", "nyc",
    "remote", "united states", "us ", "usa", "u.s.", "anywhere in the us",
]

# Non-US locations that should be hard-rejected
NON_US_SIGNALS = [
    "gurugram", "india", "dublin", "ireland", "london", "uk", "united kingdom",
    "mexico city", "mexico", "tbilisi", "georgia, ge", "singapore", "australia",
    "canada", "toronto", "vancouver", "berlin", "germany", "paris", "france",
    "amsterdam", "netherlands", "bangalore", "hyderabad", "pune", "chennai",
    "sydney", "melbourne", "dubai", "uae", "philippines", "manila",
]

# ── Title tiers ───────────────────────────────────────────────────────────────
TITLE_STRONG = [
    "business operations analyst", "engineering operations analyst",
    "technical operations analyst", "operations analyst",
    "ai solutions", "ai analyst", "business systems analyst",
    "gtm operations", "revenue operations", "sales operations analyst",
    "data operations", "product operations", "business intelligence analyst",
]
TITLE_MODERATE = [
    "data analyst", "data scientist", "business analyst",
    "program analyst", "analytics engineer", "reporting analyst",
    "insights analyst", "financial analyst",
]

# Auto-reject title prefixes/words
TITLE_SENIOR_REJECT = [
    "senior ", "sr.", "sr ", "staff ", "principal ", "lead ",
    "director", "manager", "head of", "vp ", "vice president",
    "chief", "president", "partner",
]

# ── Description keyword weights ───────────────────────────────────────────────
# Recalibrated — single keyword can't push to 10 alone
DESC_POSITIVE = {
    # Core technical (1.5 pts each — was 2)
    "python": 1.5, "sql": 1.5, "tableau": 1.5, "power bi": 1.5,
    "pandas": 1.5, "etl": 1.5, "airflow": 1.5,

    # Dashboard/pipeline (1 pt each)
    "dashboard": 1.0, "pipeline": 1.0, "kpi": 1.0, "reporting": 1.0,

    # Role fit signals (1.5 pts each)
    "cross-functional": 1.5, "stakeholder": 1.0,
    "operational efficiency": 1.5, "business operations": 1.5,
    "process improvement": 1.5, "demand forecasting": 1.5,
    "capacity planning": 1.5, "data quality": 1.5,
    "data validation": 1.5,

    # Nice to have (0.5 pts)
    "llm": 0.5, "automation": 0.5, "machine learning": 0.5,
    "docker": 0.5, "aws": 0.5, "excel": 0.5,
    "data visualization": 0.5, "a/b test": 0.5,
    "forecasting": 0.5, "analytics": 0.5, "insight": 0.5,
}

DESC_NEGATIVE = {
    "5+ years": -2, "7+ years": -3, "10+ years": -4,
    "c++": -1.5, "cuda": -3, "kubernetes": -0.5,
    "embedded": -2, "hardware": -2, "phd required": -3,
    "clearance": -2, "secret clearance": -3,
}

# ── Resume variant map ────────────────────────────────────────────────────────
VARIANT_MAP = {
    "business operations": "biz_ops", "engineering operations": "eng_ops",
    "technical operations": "eng_ops", "operations analyst": "biz_ops",
    "ai solutions": "ai_solutions", "ai analyst": "ai_solutions",
    "gtm": "ai_solutions", "revenue operations": "ai_solutions",
    "sales operations": "ai_solutions", "data scientist": "data_science",
    "data science": "data_science", "data analyst": "data_analyst",
    "business analyst": "biz_ops", "business systems": "biz_ops",
    "business intelligence": "eng_ops", "financial analyst": "biz_ops",
}

RESUME_FILES = {
    "biz_ops":      "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":      "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science": "Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions": "Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst": "Jason_Gu_Disney_DataAnalyst_Color.docx",
}


def _is_us_location(location: str) -> bool:
    """True if location is in the US or remote."""
    if not location:
        return True     # unknown — let through, score will be lower
    loc = location.lower()

    # Hard reject non-US first
    for signal in NON_US_SIGNALS:
        if signal in loc:
            return False

    # Must match at least one US signal
    for state in US_STATES:
        if state in loc:
            return True

    # No match — likely international
    return False


def _is_too_senior(title: str) -> bool:
    t = title.lower()
    return any(prefix in t for prefix in TITLE_SENIOR_REJECT)


def _pick_variant(title: str) -> str:
    t = title.lower()
    for pattern, variant in VARIANT_MAP.items():
        if pattern in t:
            return variant
    return "biz_ops"


def _score_job(job: dict) -> dict | None:
    """
    Score a job. Returns None if location or seniority check fails.
    """
    title    = job.get("title", "")
    location = job.get("location", "")

    # ── Hard filters ──────────────────────────────────────────────────────────
    if not _is_us_location(location):
        log.debug("  [SKIP - non-US] %s @ %s (%s)", title, job["company"], location)
        return None

    if _is_too_senior(title):
        log.debug("  [SKIP - senior] %s @ %s", title, job["company"])
        return None

    # ── Scoring ───────────────────────────────────────────────────────────────
    title_l  = title.lower()
    desc     = (job.get("description", "") or "").lower()
    combined = title_l + " " + desc

    score   = 0.0
    reasons = []

    # Title tier
    strong_hit = False
    for kw in TITLE_STRONG:
        if kw in title_l:
            score += 3.5
            strong_hit = True
            reasons.append(f"Title is a strong match for your target role type")
            break
    if not strong_hit:
        for kw in TITLE_MODERATE:
            if kw in title_l:
                score += 1.5
                reasons.append(f"Title is a reasonable fit")
                break

    # Description keywords
    matched_pos, matched_neg = [], []
    for kw, pts in DESC_POSITIVE.items():
        if kw in combined:
            score += pts
            matched_pos.append(kw)
    for kw, pts in DESC_NEGATIVE.items():
        if kw in combined:
            score += pts
            matched_neg.append(kw)

    # Build reasons
    top_skills = [k for k in matched_pos if k in (
        "python","sql","tableau","power bi","etl","kpi",
        "dashboard","pipeline","airflow","stakeholder","cross-functional",
        "demand forecasting","data quality","data validation"
    )]
    if top_skills:
        reasons.append(f"Core skills match: {', '.join(top_skills[:5])}")

    ops_signals = [k for k in matched_pos if k in (
        "business operations","operational efficiency","process improvement",
        "capacity planning","data quality","data validation"
    )]
    if ops_signals:
        reasons.append(f"Ops signals match your Helport/SDG&E background: {', '.join(ops_signals[:3])}")

    if matched_neg:
        reasons.append(f"⚠️ Watch: {', '.join(matched_neg[:3])}")

    if len(reasons) == 0:
        reasons.append("Keyword overlap with your technical profile")

    score = max(1, min(10, round(score)))

    variant = _pick_variant(title)

    return {
        **job,
        "score":          score,
        "match_reasons":  reasons[:3],
        "resume_variant": variant,
        "resume_file":    RESUME_FILES.get(variant, RESUME_FILES["biz_ops"]),
        "concern":        ", ".join(matched_neg) if matched_neg else "",
    }


def score_jobs_batch(jobs: list[dict], min_score: int = 6) -> list[dict]:
    """
    Score all jobs. Filters non-US and senior roles before scoring.
    Deduplicates by (company + title) to prevent repeat entries.
    Returns only jobs meeting min_score, sorted best first.
    """
    scored    = []
    seen_keys = set()

    for job in jobs:
        result = _score_job(job)
        if result is None:
            continue

        # Deduplicate by company + normalized title
        dedup_key = f"{result['company'].lower()}|{result['title'].lower().strip()}"
        if dedup_key in seen_keys:
            log.debug("  [SKIP - duplicate] %s @ %s", result["title"], result["company"])
            continue
        seen_keys.add(dedup_key)

        log.info("  [%d/10] %s @ %s (%s)",
                 result["score"], result["title"],
                 result["company"], result.get("location", "?"))

        if result["score"] >= min_score:
            scored.append(result)

    return sorted(scored, key=lambda x: x["score"], reverse=True)
