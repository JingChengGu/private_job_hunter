"""
matcher.py v5 - ML/AI engineering roles added, RAG/LangChain hold logic,
Databricks/Scale/Palantir FDE blocked, lookback 9 days (5 business days)
Vancouver NOT added (requires Canadian work permit)
"""
import re
import logging

log = logging.getLogger(__name__)

HARD_NON_US = [
    "india","ireland","united kingdom","england","germany","france",
    "netherlands","switzerland","sweden","spain","italy","poland","czech",
    "mexico","canada","brazil","colombia","argentina",
    "singapore","australia","japan","china","korea","taiwan",
    "hong kong","philippines","indonesia","malaysia","thailand",
    "dubai","uae","israel","egypt","south africa","kenya",
    "bengaluru","bangalore","gurugram","gurgaon","hyderabad","pune",
    "mumbai","delhi","new delhi","noida","chennai","kolkata",
    "tbilisi","toronto","vancouver","montreal","sydney","melbourne",
    "tokyo","beijing","shanghai","seoul","taipei",
    "london","dublin","berlin","paris","amsterdam","zurich",
    "stockholm","madrid","milan","warsaw","prague",
    "sao paulo","bogota","buenos aires",
    ", uk","- uk",
]

US_CONFIRMED = [
    "san diego","san francisco","los angeles","new york city","nyc",
    "seattle","austin","boston","chicago","denver","atlanta",
    "miami","san jose","mountain view","palo alto","menlo park",
    "redwood city","santa clara","sunnyvale","cupertino","burbank",
    "irvine","san mateo","bellevue","kirkland","portland",
    "salt lake city","phoenix","dallas","houston","raleigh",
    "charlotte","nashville","minneapolis","detroit","brooklyn",
    "san antonio","sacramento","fresno","long beach","pasadena",
    "united states","usa","u.s.","remote","work from home",
    "nationwide","anywhere in the us",
    "california","new york state","texas","washington state",
    "illinois","massachusetts","colorado","florida","oregon",
    "nevada","arizona","north carolina","south carolina",
    "virginia","michigan","ohio","utah","minnesota","wisconsin",
    "tennessee","maryland","new jersey","pennsylvania","indiana",
    ", ca ",", ca,",", ca."," ca,",
    ", ny ",", ny,",", tx ",", tx,",
    ", wa ",", wa,",", il ",", il,",
    ", ma ",", ma,",", co ",", co,",
    ", fl ",", fl,",", or ",", or,",
    ", nv ",", nv,",", az ",", az,",
    ", nc ",", nc,",", va ",", va,",
    "atlanta, georgia","georgia, us","georgia, usa",
]

# ── San Diego / domain company boost ─────────────────────────────────────────
# These are mid-size domain companies (medical device, defense, biotech, healthtech)
# adopting AI — the ATEC Spine archetype. Boost score +1 when matched.
SD_DOMAIN_COMPANIES = [
    "alphatec", "atec spine", "resmed", "dexcom", "tandem diabetes",
    "illumina", "neurocrine", "viasat", "leidos", "booz allen", "saic",
    "cubic", "xifin", "mitchell", "shield ai", "vannevar", "tusimple",
    "artera", "benchling", "veracyte", "syntiant", "neuralmagic",
    "kitware", "covariant", "mendaera", "axonics", "relativity space",
    "terray", "vividion", "accolade", "collective health", "oura",
    "hims", "sony", "kyocera", "teradata",
]

SD_LOCATIONS = [
    "san diego", "carlsbad", "la jolla", "del mar", "solana beach",
    "encinitas", "oceanside", "escondido", "el cajon", "chula vista",
    "national city", "coronado", "santee", "poway", "miramar",
    "sorrento valley", "torrey pines", "north county", "san marcos",
    "vista", "camp pendleton",
]




# Strong US signals = actual cities/states — used for multi-city exception
STRONG_US = [
    "san diego","san francisco","los angeles","new york city","nyc","new york, ny",
    "seattle","austin","boston","chicago","denver","atlanta","miami","san jose",
    "mountain view","palo alto","santa clara","sunnyvale","cupertino","burbank",
    "irvine","san mateo","bellevue","kirkland","portland","salt lake city","phoenix",
    "dallas","houston","raleigh","charlotte","nashville","minneapolis","detroit",
    "brooklyn","san antonio","sacramento","redwood city","menlo park",
    "california","new york state","texas","washington state","illinois",
    "massachusetts","colorado","florida","oregon","nevada","arizona",
    "north carolina","south carolina","virginia","michigan","ohio","utah",
    "minnesota","wisconsin","tennessee","maryland","new jersey","pennsylvania",
    "united states","usa","u.s.","work from home","nationwide","anywhere in the us",
    "atlanta, georgia","georgia, us",
    ", ca ",", ca,",", ca."," ca,",", ny ",", ny,",", tx ",", tx,",
    ", wa ",", wa,",", il ",", il,",", ma ",", ma,",", co ",", co,",
    ", fl ",", fl,",", or ",", or,",", nv ",", nv,",", az ",", az,",
    ", nc ",", nc,",", va ",", va,",
]


def _is_us_location(location):
    """
    Non-US check runs FIRST, unconditionally.
    'Remote - India' -> has_non_us=True, no STRONG US signal -> False
    'NY, SF, Sao Paulo' -> has_non_us=True, has STRONG US signal -> True (multi-city role)
    'Remote' -> no non-US, has weak US -> True
    """
    if not location or location.strip() == "":
        return True

    loc = " " + location.lower() + " "

    has_non_us    = any(sig in loc for sig in HARD_NON_US)
    has_strong_us = (any(sig in loc for sig in STRONG_US) or
                     bool(re.search(r",\s*(ca|ny|tx|wa|il|ma|co|ga|fl|or|nv|az|nc|va|ut|mn|wi|in|tn|md|nj|pa)\s*$",
                                    location.lower())))
    has_weak_us   = "remote" in loc or "work from home" in loc

    # Non-US present + no strong US city/state = reject
    # (catches "Remote - India", "Poland Remote", "India Remote")
    if has_non_us and not has_strong_us:
        return False

    # Strong US city/state present = accept
    # (catches multi-city "NY, SF, Sao Paulo" — role is open to US)
    if has_strong_us:
        return True

    # Weak US signal only ("Remote", "Work from Home") with no non-US = accept
    if has_weak_us:
        return True

    # No signal = reject
    return False


HOLD_COMBOS = [
    ("databricks",   "forward deployed"),
    ("scale ai",     "forward deployed"),
    ("palantir",     "forward deployed"),
    ("databricks",   "field data engineer"),
    ("databricks",   "fde"),
]

HOLD_DESC_PATTERNS = [
    r"experience\s+with\s+langchain",
    r"langchain\s+(experience|required|proficiency|expertise)",
    r"rag\s+(experience|required|proficiency|expertise|pipeline required)",
    r"retrieval.augmented\s+generation\s+(experience|required)",
    r"multi.agent\s+(experience|required|systems\s+required)",
    r"(required|must have|must know)[^.]*langchain",
    r"(required|must have|must know)[^.]*multi.agent",
]


def _is_on_hold(job):
    company = job.get("company","").lower()
    title   = job.get("title","").lower()
    desc    = (job.get("description","") or "").lower()
    for co, role in HOLD_COMBOS:
        if co in company and role in title:
            return True
    for pattern in HOLD_DESC_PATTERNS:
        if re.search(pattern, desc):
            return True
    return False


# Highest-priority target roles — score +5.0 base (vs +3.5 for TITLE_STRONG)
TITLE_PRIORITY = [
    "forward deployed engineer",
    "forward deployed",
    "ai solutions engineer",
    "ai sales engineer",
    "sales engineer",
]

TITLE_STRONG = [
    "ml engineer","mlops engineer","ai/ml engineer",
    "applied ai engineer","applied ml engineer",
    "ai platform engineer","ai infrastructure engineer",
    "machine learning engineer",
    "software engineer, ai","software engineer - ai","software engineer ai",
    "software engineer, ml","software engineer - ml","software engineer ml",
    "backend engineer, ml","backend engineer - ml","backend engineer ml",
    "ai implementation engineer",
    "technical customer success engineer",
    "business operations analyst","engineering operations analyst",
    "technical operations analyst","operations analyst",
    "gtm operations","revenue operations analyst",
    "sales operations analyst","data operations analyst",
    "product operations analyst","business intelligence analyst",
    "business systems analyst",
    "implementation engineer","solutions engineer",
    "ai analyst","applied ai",
]

TITLE_MODERATE = [
    "data analyst","data scientist","business analyst",
    "program analyst","analytics engineer","reporting analyst",
    "insights analyst","data engineer",
    "operations specialist","implementation specialist",
    "technical analyst","product analyst",
    "machine learning","ml platform",
    "ai engineer","nlp engineer",
    "software engineer","solutions architect",
]

TITLE_SENIOR_REJECT = [
    "senior ","sr.","sr ","staff ","principal ",
    "lead ","director","manager","head of",
    "vp ","vice president","chief","president","partner",
]

DESC_POSITIVE = {
    "python":2.0,"sql":1.5,"tableau":1.5,"power bi":1.5,
    "pandas":1.5,"etl":1.5,"airflow":1.5,
    "dashboard":1.0,"pipeline":1.0,"kpi":1.0,"reporting":1.0,
    "data quality":1.0,"data validation":1.0,
    "cross-functional":1.5,"stakeholder":1.0,
    "business operations":1.5,"process improvement":1.5,
    "llm":2.0,"large language model":2.0,"generative ai":2.0,
    "ai agent":2.0,"prompt engineering":1.5,
    "fine-tuning":1.5,"fine tuning":1.5,
    "pytorch":2.0,"tensorflow":1.5,"transformers":1.5,
    "hugging face":1.5,"inference":2.0,"deployment":1.5,
    "model serving":2.0,"model optimization":2.0,
    "mlops":2.0,"ml pipeline":2.0,"ml platform":2.0,
    "vector database":1.5,"embeddings":1.5,
    "scikit":1.0,"xgboost":1.0,
    "docker":1.0,"aws":0.5,"google cloud":0.5,
    "fastapi":1.0,"rest api":1.0,
    "machine learning":1.5,"deep learning":1.5,
    "automation":1.0,"workflow automation":1.5,
    "implementation":1.0,"production":1.0,
    "excel":0.5,"data visualization":0.5,"a/b test":0.5,
    "analytics":0.5,"forecasting":0.5,
}

DESC_NEGATIVE = {
    "5+ years":-2.0,"7+ years":-3.0,"10+ years":-4.0,
    "c++":-1.5,"cuda":-0.5,
    "embedded":-2.0,"firmware":-3.0,"hardware":-2.0,
    "phd required":-3.0,"phd preferred":-1.0,
    "clearance":-2.0,"secret clearance":-3.0,
    "financial modeling":-1.0,"gaap":-1.5,
    "verilog":-3.0,"fpga":-3.0,"asic":-3.0,
}

VARIANT_MAP = {
    "ml engineer":"data_science","mlops":"data_science",
    "ai/ml":"data_science","applied ai":"data_science",
    "applied ml":"data_science","ai platform":"data_science",
    "ai infrastructure":"data_science","machine learning":"data_science",
    "software engineer":"data_science","backend engineer":"data_science",
    "nlp":"data_science","data engineer":"data_science",
    "analytics engineer":"data_science",
    "ai solutions":"ai_solutions","ai analyst":"ai_solutions",
    "ai sales":"ai_solutions","sales engineer":"ai_solutions",
    "forward deployed":"ai_solutions","implementation":"ai_solutions",
    "solutions engineer":"ai_solutions","gtm":"ai_solutions",
    "revenue operations":"ai_solutions","sales operations":"ai_solutions",
    "customer success":"ai_solutions",
    "business operations":"biz_ops","engineering operations":"eng_ops",
    "technical operations":"eng_ops","operations analyst":"biz_ops",
    "business analyst":"biz_ops","business systems":"biz_ops",
    "business intelligence":"eng_ops",
    "data scientist":"data_science","data science":"data_science",
    "data analyst":"data_analyst","reporting analyst":"data_analyst",
}

RESUME_FILES = {
    "biz_ops":     "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":     "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science":"Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions":"Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst":"Jason_Gu_Disney_DataAnalyst_Color.docx",
}


def _is_too_senior(title):
    t = title.lower()
    return any(p in t for p in TITLE_SENIOR_REJECT)


def _pick_variant(title):
    t = title.lower()
    for pattern, variant in VARIANT_MAP.items():
        if pattern in t: return variant
    return "biz_ops"


def _score_job(job):
    title    = job.get("title","")
    location = job.get("location","")
    if not _is_us_location(location):
        log.debug("  [SKIP non-US] %s @ %s", title, job["company"]); return None
    if _is_too_senior(title):
        log.debug("  [SKIP senior] %s @ %s", title, job["company"]); return None
    if _is_on_hold(job):
        log.debug("  [SKIP hold]   %s @ %s", title, job["company"]); return None

    title_l  = title.lower()
    desc     = (job.get("description","") or "").lower()
    combined = title_l + " " + desc
    score    = 0.0
    reasons  = []

    if any(kw in title_l for kw in TITLE_PRIORITY):
        score += 5.0; reasons.append("Priority target role: forward deployed / AI solutions / AI sales")
    elif any(kw in title_l for kw in TITLE_STRONG):
        score += 3.5; reasons.append("Title is a strong match for your target role type")
    elif any(kw in title_l for kw in TITLE_MODERATE):
        score += 1.5; reasons.append("Title is a reasonable fit")

    matched_pos, matched_neg = [], []
    for kw, pts in DESC_POSITIVE.items():
        if kw in combined: score += pts; matched_pos.append(kw)
    for kw, pts in DESC_NEGATIVE.items():
        if kw in combined: score += pts; matched_neg.append(kw)

    top = [k for k in matched_pos if k in (
        "python","sql","pytorch","tensorflow","llm","ai agent","mlops",
        "inference","model serving","model optimization","ml pipeline",
        "transformers","fine-tuning","vector database","embeddings",
        "tableau","etl","machine learning","deep learning","fastapi",
    )]
    if top: reasons.append(f"Core skills match: {chr(44).join(top[:5])}")

    ml = [k for k in matched_pos if k in (
        "llm","pytorch","inference","model serving","mlops",
        "generative ai","ai agent","transformers","fine-tuning",
    )]
    if ml: reasons.append(f"ML/AI signals: {chr(44).join(ml[:3])}")

    if matched_neg: reasons.append(f"Watch: {chr(44).join(matched_neg[:3])}")
    if not reasons: reasons.append("Keyword overlap with your technical profile")

    # Boost for SD-area domain companies (ATEC Spine archetype)
    company_lower = job.get("company","").lower()
    if any(sd in company_lower for sd in SD_DOMAIN_COMPANIES):
        score = min(10, score + 1)
        if "Domain company adopting AI" not in " ".join(reasons):
            reasons.insert(0, "Domain company adopting AI (ATEC Spine archetype) — high callback potential")

    # Boost for San Diego location
    if any(sd in location.lower() for sd in SD_LOCATIONS):
        score = min(10, score + 0.5)

    # Quality gate: require meaningful description match
    # Title-only matches never reach inbox (no skills = noise)
    if not matched_pos:
        return None   # zero description keywords = skip entirely
    # Require 2+ keywords for score to count as 6+
    if len(matched_pos) < 2 and score < 8:
        return None
    score   = max(1, min(10, round(score)))
    variant = _pick_variant(title)
    return {
        **job,
        "score":score,"match_reasons":reasons[:3],
        "resume_variant":variant,
        "resume_file":RESUME_FILES.get(variant,RESUME_FILES["biz_ops"]),
        "concern":chr(44).join(matched_neg) if matched_neg else "",
    }


def score_jobs_batch(jobs, min_score=6):
    scored = []; seen = set()
    for job in jobs:
        r = _score_job(job)
        if r is None: continue
        k = f"{r['company'].lower()}|{r['title'].lower().strip()}"
        if k in seen: continue
        seen.add(k)
        log.info("  [%d/10] %s @ %s (%s)", r["score"], r["title"], r["company"], r.get("location","?"))
        if r["score"] >= min_score: scored.append(r)
    return sorted(scored, key=lambda x: x["score"], reverse=True)
