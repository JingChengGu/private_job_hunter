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
        {"name": "ResMed",          "slug": "resmed"},
        {"name": "Viasat",          "slug": "viasat"},
    ],
    "workday": [
        {"name": "Qualcomm",         "subdomain": "qualcomm",         "site_num": "5",  "tenant": "qualcomm_career"},
        {"name": "Disney",           "subdomain": "disney",           "site_num": "5",  "tenant": "disneycareer"},
        {"name": "Salesforce",       "subdomain": "salesforce",       "site_num": "12", "tenant": "External_Career_Site"},
        {"name": "Adobe",            "subdomain": "adobe",            "site_num": "5",  "tenant": "external_corporate"},
        {"name": "Palo Alto Networks","subdomain": "paloaltonetworks","site_num": "1",  "tenant": "PaloAltoNetworks"},
        {"name": "ServiceNow",       "subdomain": "servicenow",       "site_num": "5",  "tenant": "servicenow"},
        {"name": "Visa",             "subdomain": "visa",             "site_num": "5",  "tenant": "visa"},
        {"name": "Intuit",           "subdomain": "intuit",           "site_num": "5",  "tenant": "careers"},
        {"name": "Nvidia",           "subdomain": "nvidia",           "site_num": "5",  "tenant": "NVIDIAExternalCareerSite"},
        {"name": "Cisco",            "subdomain": "cisco",            "site_num": "5",  "tenant": "Cisco"},
        {"name": "Intel",            "subdomain": "intel",            "site_num": "5",  "tenant": "intel"},
        {"name": "Oracle",           "subdomain": "oracle",           "site_num": "5",  "tenant": "oracle"},
        {"name": "Uber",             "subdomain": "uber",             "site_num": "5",  "tenant": "uberats"},
        {"name": "Airbnb",           "subdomain": "airbnb",           "site_num": "5",  "tenant": "Airbnb"},
        {"name": "DoorDash",         "subdomain": "doordash",         "site_num": "5",  "tenant": "DoorDashUSA"},
        {"name": "Lyft",             "subdomain": "lyft",             "site_num": "5",  "tenant": "lyft"},
        {"name": "Snowflake",        "subdomain": "snowflake",        "site_num": "5",  "tenant": "Snowflake"},
        {"name": "Workday",          "subdomain": "workday",          "site_num": "5",  "tenant": "workday"},
        {"name": "SAP",              "subdomain": "sap",              "site_num": "5",  "tenant": "SAP"},
        {"name": "CrowdStrike",      "subdomain": "crowdstrike",      "site_num": "5",  "tenant": "crowdstrike"},
        {"name": "Okta",             "subdomain": "okta",             "site_num": "5",  "tenant": "okta"},
        {"name": "Splunk",           "subdomain": "splunk",           "site_num": "5",  "tenant": "splunk"},
        {"name": "Zendesk",          "subdomain": "zendesk",          "site_num": "5",  "tenant": "zendesk"},
        {"name": "Atlassian",        "subdomain": "atlassian",        "site_num": "5",  "tenant": "atlassian"},
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
