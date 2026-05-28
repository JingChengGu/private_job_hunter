"""
Job Hunter Configuration — Jason Gu
"""

JASON_PROFILE = """
CANDIDATE: Jason Gu
EDUCATION: B.S. Data Science, UC San Diego
AUTHORIZATION: U.S. Citizen

CURRENT ROLE: AI Solutions Engineer / Technical Project Manager @ Helport AI (July 2025–Present)
- Managed AI-assisted outbound sales operations across Philippines, Mexico, Bolivia
- Oversaw 50+ agents, 4 operations managers, 10+ concurrent U.S. SMB clients
- Built LLM-powered agent workflow systems for live outbound sales execution
- Built KPI dashboards tracking conversion rates, call volume, quality metrics
- Cross-functional bridge between executives, clients, offshore leadership, tech systems

PRIOR EXPERIENCE:
- Data Science Fellow @ SDG&E: Python/SQL pipelines, 1,100+ EV charger deployments,
  XGBoost forecasting, Tableau dashboards, weekly stakeholder reports
- Data Science Intern @ Mercury Alert AI: QA dashboard, ETL pipeline (40% error reduction),
  AWS QuickSight anomaly detection, AWS Lambda (30% efficiency gain)
- Data Analyst Intern @ Redrock Biometrics: OpenCV/NumPy pipeline, KNN optimization (FNR -63.6%),
  Python/SQL/Tableau business strategy analysis

TECHNICAL SKILLS:
Python, SQL/PostgreSQL, Pandas, NumPy, Scikit-Learn, XGBoost, LightGBM
Tableau, Power BI, Dash/Plotly, Excel
Apache Airflow, Docker, AWS, Google Cloud, GitHub
LLM Integration, AI Agents, Prompt Engineering, NLP, ETL Pipeline Development

BEST FIT ROLES:
1. Business / Engineering / Technical Operations Analyst
2. AI Solutions Engineer / AI Implementation Analyst
3. Data Analyst (ops-focused)
4. Forward Deployed Engineer / Solutions Engineer
5. GTM / Revenue / Sales Operations Analyst
6. Data Scientist (applied, not research)
7. Business Systems / Process Automation Analyst
8. AI/ML Implementation Specialist
"""

# ── Target companies ──────────────────────────────────────────────────────────

TARGET_COMPANIES = {
    "greenhouse": [
        # Core AI / data companies
        {"name": "Databricks",      "slug": "databricks"},
        {"name": "Scale AI",        "slug": "scaleai"},
        {"name": "Hugging Face",    "slug": "huggingface"},
        {"name": "Cohere",          "slug": "cohere"},
        {"name": "Weights & Biases","slug": "wandb"},
        {"name": "Together AI",     "slug": "togetherai"},
        {"name": "Perplexity AI",   "slug": "perplexityai"},
        {"name": "Glean",           "slug": "glean"},
        {"name": "Moveworks",       "slug": "moveworks"},
        {"name": "Harvey",          "slug": "harvey"},
        {"name": "Anduril",         "slug": "anduril"},
        {"name": "Shield AI",       "slug": "shieldai"},
        # Ops / analytics companies
        {"name": "Discord",         "slug": "discord"},
        {"name": "Instawork",       "slug": "instawork"},
        {"name": "GoodLeap",        "slug": "goodleap"},
        {"name": "Samsara",         "slug": "samsara"},
        {"name": "Rippling",        "slug": "rippling"},
        {"name": "Brex",            "slug": "brex"},
        {"name": "Ramp",            "slug": "ramp"},
        {"name": "Retool",          "slug": "retool"},
        {"name": "Airtable",        "slug": "airtable"},
        {"name": "Notion",          "slug": "notion"},
        {"name": "Figma",           "slug": "figma"},
        {"name": "Loom",            "slug": "loom"},
        {"name": "Linear",          "slug": "linear"},
        {"name": "Fivetran",        "slug": "fivetran"},
        {"name": "dbt Labs",        "slug": "dbtlabs"},
        {"name": "Airbyte",         "slug": "airbyte"},
        {"name": "Hightouch",       "slug": "hightouch"},
        {"name": "Census",          "slug": "census"},
        # Enterprise / established tech
        {"name": "Okta",            "slug": "okta"},
        {"name": "CrowdStrike",     "slug": "crowdstrike"},
        {"name": "MongoDB",         "slug": "mongodb"},
        {"name": "Palantir",        "slug": "palantir"},
        {"name": "Covariant",       "slug": "covariant"},
        {"name": "Nuro",            "slug": "nuro"},
        {"name": "Zipline",         "slug": "zipline"},
        # San Diego / domain companies on Greenhouse
        {"name": "Mendaera",        "slug": "mendaera"},       # surgical robotics, La Jolla
        {"name": "Axonics",         "slug": "axonics"},        # medical device, Irvine
        {"name": "Acutus Medical",  "slug": "acutusmedical"},  # cardiac, Carlsbad
        {"name": "Classy",          "slug": "classy"},         # nonprofit SaaS, San Diego
        {"name": "Manpower Group",  "slug": "manpowergroup"},  # workforce, SD office
        {"name": "Woofware",        "slug": "woofware"},
        {"name": "Vericel",         "slug": "vericel"},
        {"name": "ServiceMax",      "slug": "servicemax"},     # field service AI
        {"name": "Artera",          "slug": "artera"},         # healthcare AI, SD
        {"name": "Oura",            "slug": "ouraring"},       # health wearable
        {"name": "Hims & Hers",     "slug": "forhims"},        # healthtech
        {"name": "Lively",          "slug": "lively"},
        {"name": "Netsmart",        "slug": "netsmart"},
        {"name": "Accolade",        "slug": "accolade"},       # health navigation
        {"name": "Solera Health",   "slug": "solerahealth"},
        {"name": "Collective Health","slug": "collectivehealth"},
        {"name": "Relativity Space","slug": "relativityspace"},# aerospace, LA
        {"name": "Shield AI",       "slug": "shieldai"},       # defense AI, SD
        {"name": "Vannevar Labs",   "slug": "vannevarlabs"},   # defense AI, SD
        {"name": "Kitware",         "slug": "kitware"},        # scientific computing
        {"name": "TuSimple",        "slug": "tusimple"},       # autonomous, SD
        {"name": "Terray Therapeutics","slug": "terraytherapeutics"},  # biotech AI
        {"name": "Vividion Therapeutics","slug": "vividiontherapeutics"},
    ],
    "lever": [
        {"name": "Stripe",          "slug": "stripe"},
        {"name": "Thumbtack",       "slug": "thumbtack"},
        {"name": "ServiceTitan",    "slug": "servicetitan"},
        {"name": "Carta",           "slug": "carta"},
        {"name": "OpenAI",          "slug": "openai"},
        {"name": "Anthropic",       "slug": "anthropic"},
        {"name": "Mistral AI",      "slug": "mistral"},
        {"name": "Character AI",    "slug": "characterai"},
        {"name": "Inflection AI",   "slug": "inflection"},
        {"name": "Runway",          "slug": "runwayml"},
        {"name": "Luma AI",         "slug": "lumalabs"},
        {"name": "Replit",          "slug": "replit"},
        {"name": "Vercel",          "slug": "vercel"},
        {"name": "Prefect",         "slug": "prefect"},
        {"name": "GoodLeap",        "slug": "goodleap"},
        {"name": "Viasat",          "slug": "viasatcareers"},
        # San Diego domain companies on Lever
        {"name": "Provide Financial","slug": "xifin"},
        {"name": "Artera AI",       "slug": "artera"},
        {"name": "Neuralmagic",     "slug": "neuralmagic"},   # model optimization
        {"name": "Syntiant",        "slug": "syntiant"},      # edge AI, Irvine
        {"name": "Haivision",       "slug": "haivision"},
        {"name": "Telnyx",          "slug": "telnyx"},
        {"name": "Benchling",       "slug": "benchling"},     # biotech SaaS
        {"name": "Veracyte",        "slug": "veracyte"},      # genomics, SD
        {"name": "ViaCyte",         "slug": "viacyte"},
        {"name": "Boundless Bio",   "slug": "boundlessbio"},
        {"name": "Turning Point Therapeutics","slug": "turningpoint"},
    ],
    "workday": [
        # Big tech (keep — good signal volume)
        {"name": "Qualcomm",            "subdomain": "qualcomm",         "site_num": "5",  "tenant": "qualcomm_career"},
        {"name": "Salesforce",          "subdomain": "salesforce",       "site_num": "12", "tenant": "External_Career_Site"},
        {"name": "Adobe",               "subdomain": "adobe",            "site_num": "5",  "tenant": "external_corporate"},
        {"name": "Palo Alto Networks",  "subdomain": "paloaltonetworks", "site_num": "1",  "tenant": "PaloAltoNetworks"},
        {"name": "ServiceNow",          "subdomain": "servicenow",       "site_num": "5",  "tenant": "servicenow"},
        {"name": "Visa",                "subdomain": "visa",             "site_num": "5",  "tenant": "visa"},
        {"name": "Intuit",              "subdomain": "intuit",           "site_num": "5",  "tenant": "careers"},
        {"name": "Nvidia",              "subdomain": "nvidia",           "site_num": "5",  "tenant": "NVIDIAExternalCareerSite"},
        {"name": "Cisco",               "subdomain": "cisco",            "site_num": "5",  "tenant": "Cisco"},
        {"name": "Snowflake",           "subdomain": "snowflake",        "site_num": "5",  "tenant": "Snowflake"},
        {"name": "Zendesk",             "subdomain": "zendesk",          "site_num": "5",  "tenant": "zendesk"},
        {"name": "Atlassian",           "subdomain": "atlassian",        "site_num": "5",  "tenant": "atlassian"},
        {"name": "Splunk",              "subdomain": "splunk",           "site_num": "5",  "tenant": "splunk"},
        # San Diego / North County mid-size — medical device, defense, biotech, healthtech
        # ATEC Spine archetype: domain company adopting AI, 200-2000 employees
        {"name": "Alphatec Spine",      "subdomain": "alphatec",         "site_num": "5",  "tenant": "alphatecspine"},
        {"name": "ResMed",              "subdomain": "resmed",           "site_num": "5",  "tenant": "resmed"},
        {"name": "Tandem Diabetes",     "subdomain": "tandemdiabetes",   "site_num": "5",  "tenant": "tandemdiabetes"},
        {"name": "Nuvation Bio",        "subdomain": "nuvationbio",      "site_num": "5",  "tenant": "nuvationbio"},
        {"name": "Illumina",            "subdomain": "illumina",         "site_num": "5",  "tenant": "illumina"},
        {"name": "Viasat",              "subdomain": "viasat",           "site_num": "5",  "tenant": "viasat"},
        {"name": "Leidos",              "subdomain": "leidos",           "site_num": "5",  "tenant": "leidos"},
        {"name": "Booz Allen Hamilton", "subdomain": "bah",              "site_num": "5",  "tenant": "bah"},
        {"name": "SAIC",                "subdomain": "saic",             "site_num": "5",  "tenant": "saic"},
        {"name": "Cubic",               "subdomain": "cubic",            "site_num": "5",  "tenant": "cubic"},
        {"name": "Dexcom",              "subdomain": "dexcom",           "site_num": "5",  "tenant": "dexcom"},
        {"name": "Neurocrine",          "subdomain": "neurocrine",       "site_num": "5",  "tenant": "neurocrine"},
        {"name": "Provide Financial",   "subdomain": "xifin",            "site_num": "5",  "tenant": "xifin"},
        {"name": "Kyocera",             "subdomain": "kyoceraintl",      "site_num": "5",  "tenant": "kyoceraintl"},
        {"name": "Sony",                "subdomain": "sonyglobal",       "site_num": "5",  "tenant": "sony"},
        {"name": "Teradata",            "subdomain": "teradata",         "site_num": "5",  "tenant": "teradata"},
        {"name": "Mitchell International","subdomain": "mitchell",       "site_num": "5",  "tenant": "mitchell"},
        {"name": "Zurn Elkay",          "subdomain": "zurnelkay",        "site_num": "5",  "tenant": "zurnelkay"},
    ],
}

# ── Search keywords (sent to Workday API) ─────────────────────────────────────
SEARCH_KEYWORDS = [
    "operations analyst",
    "business operations",
    "data analyst",
    "AI solutions engineer",
    "forward deployed engineer",
    "implementation engineer",
    "solutions engineer",
    "data scientist",
    "analytics engineer",
    "AI implementation",
    "revenue operations",
    "sales operations",
    "business intelligence",
    "technical operations",
    "machine learning engineer",
]

# ── Title must contain at least one of these ──────────────────────────────────
TITLE_INCLUDE_KEYWORDS = [
    "analyst",
    "data science",
    "data scientist",
    "data engineer",
    "operations",
    "analytics",
    "intelligence",
    "ai solutions",
    "ai engineer",
    "ai implementation",
    "solutions engineer",
    "forward deployed",
    "implementation",
    "machine learning",
    "ml engineer",
]

# ── Any of these in the title = auto-reject ───────────────────────────────────
TITLE_EXCLUDE_KEYWORDS = [
    "principal",
    "staff ",
    "director",
    "vp ",
    "vice president",
    "manager",
    "head of",
    "legal",
    "attorney",
    "accountant",
    "recruiter",
    "hardware",
    "embedded",
    "firmware",
    "mechanical",
    "civil",
    "electrical",
    "intern",
    "internship",
    "financial analyst",      # too finance-specific, poor fit
    "finance analyst",
    "accounting analyst",
    "tax analyst",
    "treasury analyst",
    "actuary",
]

# ── Thresholds ────────────────────────────────────────────────────────────────
MIN_MATCH_SCORE  = 6
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
