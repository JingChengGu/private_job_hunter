"""
matcher.py — Rule-based job scorer v4
Fixed: Bengaluru/all Indian cities, ambiguous Georgia state vs country,
       financial analyst removed, AI/implementation roles added,
       score calibration, deduplication
"""
import re
import logging

log = logging.getLogger(__name__)

# ── Unambiguous non-US locations ──────────────────────────────────────────────
HARD_NON_US = [
    "india","ireland","united kingdom","england","germany","france",
    "netherlands","switzerland","sweden","spain","italy","poland","czech",
    "mexico","canada","brazil","colombia","argentina",
    "singapore","australia","japan","china","korea","taiwan",
    "hong kong","philippines","indonesia","malaysia","thailand",
    "dubai","uae","israel","egypt","south africa","kenya",
    # Indian cities (both spellings)
    "bengaluru","bangalore","gurugram","gurgaon","hyderabad","pune",
    "mumbai","delhi","new delhi","noida","chennai","kolkata",
    # Other non-US cities
    "tbilisi","toronto","vancouver","montreal","sydney","melbourne",
    "tokyo","beijing","shanghai","seoul","taipei",
    "london","dublin","berlin","paris","amsterdam","zurich",
    "stockholm","madrid","milan","warsaw","prague",
    "sao paulo","bogota","buenos aires",
    # Country suffixes
    ", uk","- uk",
]

# ── Unambiguous US locations ──────────────────────────────────────────────────
US_CONFIRMED = [
    # Major US cities (no ambiguity)
    "san diego","san francisco","los angeles","new york city","nyc",
    "seattle","austin","boston","chicago","denver","atlanta",
    "miami","san jose","mountain view","palo alto","menlo park",
    "redwood city","santa clara","sunnyvale","cupertino","burbank",
    "irvine","san mateo","bellevue","kirkland","portland",
    "salt lake city","phoenix","dallas","houston","raleigh",
    "charlotte","nashville","minneapolis","detroit","brooklyn",
    "san antonio","san bernardino","sacramento","fresno","long beach",
    # Remote / US-wide
    "united states","usa","u.s.","remote","work from home",
    "nationwide","anywhere in the us","throughout the us",
    # Full US state names (unambiguous)
    "california","new york state","texas","washington state",
    "illinois","massachusetts","colorado","florida","oregon",
    "nevada","arizona","north carolina","south carolina",
    "virginia","michigan","ohio","utah","minnesota","wisconsin",
    "tennessee","maryland","new jersey","pennsylvania","indiana",
    # State abbreviations with comma context
    ", ca ", ", ca,", ", ca.", " ca,",
    ", ny ", ", ny,", ", tx ", ", tx,",
    ", wa ", ", wa,", ", il ", ", il,",
    ", ma ", ", ma,", ", co ", ", co,",
    ", fl ", ", fl,", ", or ", ", or,",
    ", nv ", ", nv,", ", az ", ", az,",
    ", nc ", ", nc,", ", va ", ", va,",
    ", ut ", ", ut,", ", mn ", ", mn,",
    ", wi ", ", wi,", ", tn ", ", tn,",
    ", md ", ", md,", ", nj ", ", nj,",
    ", pa ", ", pa,",
    # Georgia explicitly as US state
    "atlanta, georgia","georgia, us","georgia, usa",
]


def _is_us_location(location: str) -> bool:
    """True if location is in the US or remote. Three-pass logic."""
    if not location or location.strip() == "":
        return True   # unknown = let through

    loc = " " + location.lower() + " "   # pad for boundary matching

    # Pass 1: Hard reject — unambiguous non-US
    for sig in HARD_NON_US:
        if sig in loc:
            return False

    # Pass 2: Hard accept — unambiguous US
    for sig in US_CONFIRMED:
        if sig in loc:
            return True

    # Pass 3: State abbreviation at end of string  e.g. "Burbank, CA"
    if re.search(r",\s*(ca|ny|tx|wa|il|ma|co|ga|fl|or|nv|az|nc|va|ut|mn|wi|in|tn|md|nj|pa)\s*$",
                 location.lower()):
        return True

    # No signal — assume non-US to be safe
    return False


# ── Title tiers ───────────────────────────────────────────────────────────────
TITLE_STRONG = [
    "business operations analyst","engineering operations analyst",
    "technical operations analyst","operations analyst",
    "gtm operations","revenue operations analyst","sales operations analyst",
    "data operations analyst","product operations analyst",
    "business intelligence analyst","business systems analyst",
    "ai solutions engineer","ai implementation",
    "forward deployed engineer","forward deployed",
    "solutions engineer","implementation engineer",
    "ai analyst","applied ai",
]
TITLE_MODERATE = [
    "data analyst","data scientist","business analyst",
    "program analyst","analytics engineer","reporting analyst",
    "insights analyst","data engineer","machine learning engineer",
    "ml engineer","operations specialist","implementation specialist",
    "technical analyst","product analyst",
]
TITLE_SENIOR_REJECT = [
    "senior ","sr.","sr ","staff ","principal ",
    "lead ","director","manager","head of",
    "vp ","vice president","chief","president","partner",
]

# ── Keyword weights ───────────────────────────────────────────────────────────
DESC_POSITIVE = {
    "python":1.5,"sql":1.5,"tableau":1.5,"power bi":1.5,
    "pandas":1.5,"etl":1.5,"airflow":1.5,
    "dashboard":1.0,"pipeline":1.0,"kpi":1.0,"reporting":1.0,
    "data quality":1.0,"data validation":1.0,
    "cross-functional":1.5,"stakeholder":1.0,
    "operational efficiency":1.5,"business operations":1.5,
    "process improvement":1.5,"demand forecasting":1.5,
    "capacity planning":1.5,
    "llm":1.5,"large language model":1.5,"generative ai":1.5,
    "ai agent":1.5,"prompt engineering":1.5,"rag":1.5,
    "implementation":1.0,"deployment":1.0,"production":1.0,
    "automation":1.0,"workflow automation":1.5,
    "machine learning":1.0,"pytorch":1.0,"tensorflow":1.0,
    "hugging face":1.0,"scikit":0.5,"xgboost":0.5,
    "docker":0.5,"aws":0.5,"google cloud":0.5,
    "excel":0.5,"data visualization":0.5,"forecasting":0.5,
    "a/b test":0.5,"analytics":0.5,
}
DESC_NEGATIVE = {
    "5+ years":-2.0,"7+ years":-3.0,"10+ years":-4.0,
    "c++":-1.5,"cuda":-3.0,"kubernetes":-0.5,
    "embedded":-2.0,"hardware":-2.0,"phd required":-3.0,
    "clearance":-2.0,"secret clearance":-3.0,
    "financial modeling":-1.0,"gaap":-1.5,
}

# ── Resume variant map ────────────────────────────────────────────────────────
VARIANT_MAP = {
    "business operations":"biz_ops","engineering operations":"eng_ops",
    "technical operations":"eng_ops","operations analyst":"biz_ops",
    "ai solutions":"ai_solutions","ai analyst":"ai_solutions",
    "forward deployed":"ai_solutions","implementation":"ai_solutions",
    "solutions engineer":"ai_solutions","gtm":"ai_solutions",
    "revenue operations":"ai_solutions","sales operations":"ai_solutions",
    "data scientist":"data_science","data science":"data_science",
    "machine learning":"data_science","ml engineer":"data_science",
    "data engineer":"data_science","analytics engineer":"data_science",
    "data analyst":"data_analyst","business analyst":"biz_ops",
    "business systems":"biz_ops","business intelligence":"eng_ops",
}
RESUME_FILES = {
    "biz_ops":      "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":      "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science": "Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions": "Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst": "Jason_Gu_Disney_DataAnalyst_Color.docx",
}


def _is_too_senior(title: str) -> bool:
    t = title.lower()
    return any(p in t for p in TITLE_SENIOR_REJECT)


def _pick_variant(title: str) -> str:
    t = title.lower()
    for pattern, variant in VARIANT_MAP.items():
        if pattern in t:
            return variant
    return "biz_ops"


def _score_job(job: dict) -> dict | None:
    title    = job.get("title", "")
    location = job.get("location", "")

    if not _is_us_location(location):
        log.debug("  [SKIP non-US] %s @ %s — %s", title, job["company"], location)
        return None
    if _is_too_senior(title):
        log.debug("  [SKIP senior] %s @ %s", title, job["company"])
        return None

    title_l  = title.lower()
    desc     = (job.get("description", "") or "").lower()
    combined = title_l + " " + desc
    score    = 0.0
    reasons  = []

    for kw in TITLE_STRONG:
        if kw in title_l:
            score += 3.5
            reasons.append("Title is a strong match for your target role type")
            break
    else:
        for kw in TITLE_MODERATE:
            if kw in title_l:
                score += 1.5
                reasons.append("Title is a reasonable fit")
                break

    matched_pos, matched_neg = [], []
    for kw, pts in DESC_POSITIVE.items():
        if kw in combined:
            score += pts
            matched_pos.append(kw)
    for kw, pts in DESC_NEGATIVE.items():
        if kw in combined:
            score += pts
            matched_neg.append(kw)

    top_skills = [k for k in matched_pos if k in (
        "python","sql","tableau","power bi","etl","kpi","dashboard","pipeline",
        "airflow","stakeholder","cross-functional","demand forecasting",
        "data quality","data validation","llm","ai agent","prompt engineering",
        "machine learning","pytorch","implementation","workflow automation",
    )]
    if top_skills:
        reasons.append(f"Core skills match: {', '.join(top_skills[:5])}")

    ops_signals = [k for k in matched_pos if k in (
        "business operations","operational efficiency","process improvement",
        "capacity planning","data quality","data validation","workflow automation",
    )]
    if ops_signals:
        reasons.append(f"Ops signals match your Helport/SDG&E background: {', '.join(ops_signals[:3])}")

    if matched_neg:
        reasons.append(f"⚠️ Watch: {', '.join(matched_neg[:3])}")
    if not reasons:
        reasons.append("Keyword overlap with your technical profile")

    score   = max(1, min(10, round(score)))
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
    scored    = []
    seen_keys = set()
    for job in jobs:
        result = _score_job(job)
        if result is None:
            continue
        dedup_key = f"{result['company'].lower()}|{result['title'].lower().strip()}"
        if dedup_key in seen_keys:
            log.debug("  [SKIP dup] %s @ %s", result["title"], result["company"])
            continue
        seen_keys.add(dedup_key)
        log.info("  [%d/10] %s @ %s (%s)",
                 result["score"], result["title"],
                 result["company"], result.get("location","?"))
        if result["score"] >= min_score:
            scored.append(result)
    return sorted(scored, key=lambda x: x["score"], reverse=True)
