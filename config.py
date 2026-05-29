"""
Job Hunter Configuration — Jason Gu v7
Only verified ATS slugs/tenants included.
SD domain companies confirmed via direct URL check.
"""

JASON_PROFILE = """
CANDIDATE: Jason Gu | B.S. Data Science, UC San Diego | U.S. Citizen
CURRENT: AI Solutions Engineer @ Helport AI (July 2025-Present)
- Built LLM-powered agent workflow systems, managed 50+ agents, 10+ SMB clients
- Built KPI dashboards, ETL pipelines, cross-functional ops across 3 countries
PRIOR: Data Science Fellow @ SDG&E, Data Science Intern @ Mercury Alert AI,
       Data Analyst Intern @ Redrock Biometrics
SKILLS: Python, SQL, PyTorch, Pandas, Scikit-Learn, XGBoost, Tableau, Power BI,
        Airflow, Docker, AWS, LLM Integration, AI Agents, Prompt Engineering, ETL
TARGET ROLES: ML Engineer, Applied AI Engineer, AI Solutions Engineer,
              Forward Deployed Engineer, MLOps Engineer, Business Ops Analyst,
              Engineering Ops Analyst, Data Analyst (ops-focused)
"""

# ── Companies by ATS platform (ALL SLUGS VERIFIED) ───────────────────────────

TARGET_COMPANIES = {
    "greenhouse": [
        # Big tech / AI unicorns
        {"name": "Databricks",       "slug": "databricks"},
        {"name": "Discord",          "slug": "discord"},
        {"name": "Okta",             "slug": "okta"},
        {"name": "CrowdStrike",      "slug": "crowdstrike"},
        {"name": "MongoDB",          "slug": "mongodb"},
        {"name": "Samsara",          "slug": "samsara"},
        {"name": "Rippling",         "slug": "rippling"},
        {"name": "Brex",             "slug": "brex"},
        {"name": "Ramp",             "slug": "ramp"},
        {"name": "Retool",           "slug": "retool"},
        {"name": "Airtable",         "slug": "airtable"},
        {"name": "Notion",           "slug": "notion"},
        {"name": "Figma",            "slug": "figma"},
        {"name": "Fivetran",         "slug": "fivetran"},
        {"name": "dbt Labs",         "slug": "dbtlabs"},
        {"name": "Airbyte",          "slug": "airbyte"},
        {"name": "Hightouch",        "slug": "hightouch"},
        {"name": "Weights & Biases", "slug": "wandb"},
        {"name": "Glean",            "slug": "glean"},
        {"name": "Moveworks",        "slug": "moveworks"},
        {"name": "Perplexity AI",    "slug": "perplexityai"},
        {"name": "Covariant",        "slug": "covariant"},
        {"name": "Nuro",             "slug": "nuro"},
        {"name": "Zipline",          "slug": "zipline"},
        {"name": "Anduril",          "slug": "anduril"},
        # SD / domain companies — VERIFIED on Greenhouse
        {"name": "Vannevar Labs",    "slug": "vannevarlabs"},   # verified ✅
        {"name": "Shield AI",        "slug": "shieldai"},       # verified ✅ (also on Lever)
        {"name": "Oura",             "slug": "ouraring"},
        {"name": "Benchling",        "slug": "benchling"},
        {"name": "Collective Health","slug": "collectivehealth"},
        {"name": "Accolade",         "slug": "accolade"},
        {"name": "Hims & Hers",      "slug": "forhims"},
        {"name": "Kitware",          "slug": "kitware"},
        {"name": "Terray Therapeutics","slug": "terraytherapeutics"},
    ],
    "lever": [
        # Big tech / AI
        {"name": "Stripe",           "slug": "stripe"},
        {"name": "OpenAI",           "slug": "openai"},
        {"name": "Anthropic",        "slug": "anthropic"},
        {"name": "Character AI",     "slug": "characterai"},
        {"name": "Replit",           "slug": "replit"},
        {"name": "Vercel",           "slug": "vercel"},
        {"name": "Carta",            "slug": "carta"},
        {"name": "ServiceTitan",     "slug": "servicetitan"},
        {"name": "Thumbtack",        "slug": "thumbtack"},
        {"name": "GoodLeap",         "slug": "goodleap"},
        # SD / domain companies — VERIFIED on Lever
        {"name": "Shield AI",        "slug": "shieldai"},       # verified ✅
        {"name": "Vannevar Labs",    "slug": "vannevarlabs-2"}, # verified ✅ (has two slugs)
        {"name": "Viasat",           "slug": "viasat"},
        {"name": "Neuralmagic",      "slug": "neuralmagic"},
        {"name": "Syntiant",         "slug": "syntiant"},
    ],
    "workday": [
        # Big tech — verified tenants
        {"name": "Qualcomm",            "subdomain": "qualcomm",        "site_num": "5",  "tenant": "qualcomm_career"},
        {"name": "Salesforce",          "subdomain": "salesforce",      "site_num": "12", "tenant": "External_Career_Site"},
        {"name": "Adobe",               "subdomain": "adobe",           "site_num": "5",  "tenant": "external_corporate"},
        {"name": "Palo Alto Networks",  "subdomain": "paloaltonetworks","site_num": "1",  "tenant": "PaloAltoNetworks"},
        {"name": "ServiceNow",          "subdomain": "servicenow",      "site_num": "5",  "tenant": "servicenow"},
        {"name": "Visa",                "subdomain": "visa",            "site_num": "5",  "tenant": "visa"},
        {"name": "Intuit",              "subdomain": "intuit",          "site_num": "5",  "tenant": "careers"},
        {"name": "Nvidia",              "subdomain": "nvidia",          "site_num": "5",  "tenant": "NVIDIAExternalCareerSite"},
        {"name": "Cisco",               "subdomain": "cisco",           "site_num": "5",  "tenant": "Cisco"},
        {"name": "Snowflake",           "subdomain": "snowflake",       "site_num": "5",  "tenant": "Snowflake"},
        {"name": "Zendesk",             "subdomain": "zendesk",         "site_num": "5",  "tenant": "zendesk"},
        {"name": "Atlassian",           "subdomain": "atlassian",       "site_num": "5",  "tenant": "atlassian"},
        {"name": "Splunk",              "subdomain": "splunk",          "site_num": "5",  "tenant": "splunk"},
        # SD / domain companies — VERIFIED Workday URLs
        # resmed.wd3.myworkdayjobs.com/ResMed_External_Careers ✅
        {"name": "ResMed",              "subdomain": "resmed",          "site_num": "3",  "tenant": "ResMed_External_Careers"},
        # dexcom.wd1.myworkdayjobs.com/Dexcom ✅
        {"name": "Dexcom",              "subdomain": "dexcom",          "site_num": "1",  "tenant": "Dexcom"},
        # alphatecspine.wd1.myworkdayjobs.com (ATEC Spine) — verify
        {"name": "Illumina",            "subdomain": "illumina",        "site_num": "5",  "tenant": "illumina"},
        {"name": "Leidos",              "subdomain": "leidos",          "site_num": "5",  "tenant": "leidos"},
        {"name": "Booz Allen Hamilton", "subdomain": "bah",             "site_num": "5",  "tenant": "bah"},
        {"name": "SAIC",                "subdomain": "saic",            "site_num": "5",  "tenant": "saic"},
        {"name": "Viasat",              "subdomain": "viasat",          "site_num": "5",  "tenant": "viasat"},
        {"name": "Tandem Diabetes",     "subdomain": "tandemdiabetes",  "site_num": "12", "tenant": "tandemdiabetes"},  # verified ✅
    ],

    "workable": [
        # SD domain companies confirmed on Workable
        {"name": "Alphatec Spine",    "slug": "atec-spine"},       # verified ✅ apply.workable.com/atec-spine
        {"name": "Nuvation Bio",      "slug": "nuvation-bio"},
        {"name": "Artera Health",     "slug": "artera"},
        {"name": "Vividion",          "slug": "vividion-therapeutics"},
        {"name": "Solv Health",       "slug": "solv"},
        {"name": "Sorrento Therapeutics","slug": "sorrento"},
    ],
}

# ── Search keywords (Workday) ─────────────────────────────────────────────────
SEARCH_KEYWORDS = [
    "AI engineer",
    "machine learning engineer",
    "applied AI",
    "MLOps",
    "operations analyst",
    "data analyst",
    "data scientist",
    "solutions engineer",
    "forward deployed",
    "AI implementation",
    "business operations",
    "analytics engineer",
    "software engineer AI",
    "ML platform",
]

# ── Title filters ─────────────────────────────────────────────────────────────
TITLE_INCLUDE_KEYWORDS = [
    "analyst", "data science", "data scientist", "data engineer",
    "operations", "analytics", "ai solutions", "ai engineer",
    "ai implementation", "solutions engineer", "forward deployed",
    "implementation", "machine learning", "ml engineer", "mlops",
    "applied ai", "software engineer",
]

TITLE_EXCLUDE_KEYWORDS = [
    "principal", "staff ", "director", "vp ", "vice president",
    "manager", "head of", "legal", "attorney", "accountant",
    "recruiter", "hardware", "embedded", "firmware", "mechanical",
    "civil", "electrical", "intern", "internship",
    "financial analyst", "finance analyst", "accounting analyst",
    "tax analyst", "treasury analyst",
    "research engineer",   # PhD-level research — blocked
    "research scientist",  # PhD-level research — blocked
    "solutions architect", # Senior customer-facing — not a fit yet
    "specialist solutions", # Databricks SA — senior, not fit
]

# ── Thresholds ────────────────────────────────────────────────────────────────
MIN_MATCH_SCORE  = 7
MAX_YOE_REQUIRED = 5
LOOKBACK_DAYS    = 9   # 9 calendar days = 5 full business days

# ── Email ─────────────────────────────────────────────────────────────────────
EMAIL_FROM    = ""
EMAIL_TO      = ""
EMAIL_SUBJECT = "🎯 New Job Matches — {date} ({count} found)"

# ── Resume variants ───────────────────────────────────────────────────────────
RESUME_VARIANTS = {
    "biz_ops":      "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":      "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science": "Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions": "Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst": "Jason_Gu_Disney_DataAnalyst_Color.docx",
}
