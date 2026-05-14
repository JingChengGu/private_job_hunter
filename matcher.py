"""
matcher.py — Rule-based job scorer (no API required, zero cost)

Scores jobs against Jason's profile using keyword matching.
Good enough to rank and filter — paste any job here for full Claude scoring.
"""

import logging

log = logging.getLogger(__name__)

# ── Title keyword tiers ───────────────────────────────────────────────────────
TITLE_STRONG = [
    "business operations analyst", "engineering operations analyst",
    "technical operations analyst", "operations analyst",
    "ai solutions", "ai analyst", "business systems analyst",
    "gtm operations", "revenue operations", "sales operations analyst",
    "data operations", "product operations", "business intelligence analyst",
]
TITLE_MODERATE = [
    "data analyst", "data scientist", "business analyst",
    "program analyst", "analytics engineer", "reporting analyst", "insights analyst",
]

# ── Description keywords: positive weights ────────────────────────────────────
DESC_POSITIVE = {
    "python": 2, "sql": 2, "tableau": 2, "power bi": 2, "pandas": 2,
    "etl": 2, "dashboard": 2, "pipeline": 2, "kpi": 2, "airflow": 2,
    "cross-functional": 2, "stakeholder": 2, "operational efficiency": 2,
    "business operations": 2, "process improvement": 2,
    "demand forecasting": 2, "capacity planning": 2,
    "data quality": 2, "data validation": 2, "reporting": 2,
    "llm": 1, "ai": 1, "automation": 1, "machine learning": 1,
    "scikit": 1, "xgboost": 1, "docker": 1, "aws": 1,
    "google cloud": 1, "excel": 1, "data visualization": 1,
    "a/b test": 1, "forecasting": 1, "analytics": 1, "insight": 1,
}

# ── Description keywords: negative weights ────────────────────────────────────
DESC_NEGATIVE = {
    "5+ years": -2, "7+ years": -3, "10+ years": -4,
    "c++": -2, "cuda": -3, "kubernetes": -1,
    "embedded": -2, "hardware": -2, "phd": -2,
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
    "business intelligence": "eng_ops",
}

RESUME_FILES = {
    "biz_ops":      "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":      "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science": "Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions": "Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst": "Jason_Gu_Disney_DataAnalyst_Color.docx",
}


def _pick_variant(title: str) -> str:
    t = title.lower()
    for pattern, variant in VARIANT_MAP.items():
        if pattern in t:
            return variant
    return "biz_ops"


def _score_job(job: dict) -> dict:
    title    = job.get("title", "").lower()
    desc     = (job.get("description", "") or "").lower()
    combined = title + " " + desc
    score    = 0
    reasons  = []

    # Title tier
    for kw in TITLE_STRONG:
        if kw in title:
            score += 4
            reasons.append(f"Title is a strong match for your target role type")
            break
    else:
        for kw in TITLE_MODERATE:
            if kw in title:
                score += 2
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
        "dashboard","pipeline","airflow","stakeholder","cross-functional","demand forecasting"
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

    if not reasons:
        reasons.append("Keyword overlap with your technical profile")

    score   = max(1, min(10, score))
    variant = _pick_variant(job.get("title", ""))

    return {
        **job,
        "score":          score,
        "match_reasons":  reasons[:3],
        "resume_variant": variant,
        "resume_file":    RESUME_FILES.get(variant, RESUME_FILES["biz_ops"]),
        "concern":        ", ".join(matched_neg) if matched_neg else "",
    }


def score_jobs_batch(jobs: list[dict], min_score: int = 6) -> list[dict]:
    scored = []
    for job in jobs:
        result = _score_job(job)
        log.info("  [%d/10] %s @ %s", result["score"], result["title"], result["company"])
        if result["score"] >= min_score:
            scored.append(result)
    return sorted(scored, key=lambda x: x["score"], reverse=True)
