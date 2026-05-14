"""
Job Hunter Configuration
All settings, target companies, and Jason's profile live here.
Edit this file to tune the search without touching any other code.
"""

# ── Jason's profile (used by Claude API to score each job) ────────────────────
JASON_PROFILE = """
CANDIDATE: Jason Gu
EDUCATION: B.S. Data Science, UC San Diego
AUTHORIZATION: U.S. Citizen — no sponsorship needed

CURRENT ROLE: AI Solutions Engineer / Technical Project Manager
COMPANY: Helport AI, San Diego CA (July 2025 – Present)
- Managed AI-assisted outbound sales operations across Philippines, Mexico, Bolivia
- Oversaw 50+ agents across 4 operations managers, 10+ concurrent U.S. SMB clients
- Built LLM-powered agent workflow systems for live outbound sales execution
- Built and maintained performance dashboards tracking conversion rates, call volume,
  quality metrics, and disposition breakdowns
- Used data to identify conversion bottlenecks and drive daily operational decisions
- Cross-functional bridge between executives, clients, offshore leadership, tech systems

PRIOR EXPERIENCE:
- Data Science Fellow @ San Diego Gas & Electric (Sep 2024 – Mar 2025)
  → Python + SQL pipelines across 1,100+ EV charger deployments
  → ML forecasting models (XGBoost, Bayesian inference, regression)
  → Tableau dashboards for infrastructure planning decisions
  → Weekly stakeholder reports for technical and non-technical audiences
- Data Science Intern @ Mercury Alert AI (Jun 2023 – Oct 2023)
  → Built QA dashboard + automated ETL pipeline (40% error reduction)
  → AWS QuickSight anomaly detection and reporting
  → Improved model retraining efficiency by 30% via AWS Lambda
- Data Analyst Intern @ Redrock Biometrics (Jun 2022 – Sep 2022)
  → Image processing pipeline with OpenCV/NumPy
  → KNN model optimization (reduced FNR by 63.6%)
  → Business strategy analysis in Python, SQL, Tableau

TECHNICAL SKILLS:
Python, SQL/PostgreSQL, Pandas, NumPy, Scikit-Learn, XGBoost, LightGBM
Tableau, Power BI, Dash/Plotly, Excel
Apache Airflow, Docker, AWS, Google Cloud, GitHub
LLM Integration, AI Agents, Prompt Engineering, NLP, ETL Pipeline Development

BEST FIT ROLES (in priority order):
1. Business Operations Analyst
2. Engineering Operations Analyst
3. Technical Operations Analyst
4. AI Solutions Engineer / Analyst
5. GTM / Revenue Operations Analyst
6. Data Analytics Analyst (ops-focused, not pure research)
7. Business Systems Analyst
8. Sales Operations Analyst

LOCATION: San Diego CA preferred, open to relocation or remote
SALARY TARGET: $70,000+ (no cap)

STRENGTHS TO MATCH AGAINST:
- Multi-client operational ownership (Helport: 10+ clients simultaneously)
- KPI/dashboard systems from scratch
- SQL + Python data pipelines
- Cross-functional stakeholder communication (technical + non-technical)
- AI/LLM workflow automation in production
- ETL pipeline design + data quality
- Demand forecasting + capacity planning (SDG&E)
"""

# ── Target companies by ATS platform ─────────────────────────────────────────
# Workday: POST /wday/cxs/{subdomain}/{tenant}/jobs
# Greenhouse: GET https://boards-api.greenhouse.io/v1/boards/{slug}/jobs
# Lever: GET https://api.lever.co/v0/postings/{slug}?mode=json

TARGET_COMPANIES = {
    "workday": [
        # subdomain = the part before .myworkdayjobs.com
        # site_num  = the number in wd5, wd12 etc.
        # tenant    = the path segment after the subdomain in job URLs
        {
            "name": "Qualcomm",
            "subdomain": "qualcomm",
            "site_num": "5",
            "tenant": "qualcomm_career",
        },
        {
            "name": "Disney",
            "subdomain": "disney",
            "site_num": "5",
            "tenant": "disneycareer",
        },
        {
            "name": "Salesforce",
            "subdomain": "salesforce",
            "site_num": "12",
            "tenant": "External_Career_Site",
        },
        {
            "name": "Adobe",
            "subdomain": "adobe",
            "site_num": "5",
            "tenant": "external_corporate",
        },
        {
            "name": "Palo Alto Networks",
            "subdomain": "paloaltonetworks",
            "site_num": "1",
            "tenant": "PaloAltoNetworks",
        },
        {
            "name": "ServiceNow",
            "subdomain": "servicenow",
            "site_num": "5",
            "tenant": "servicenow",
        },
        {
            "name": "Visa",
            "subdomain": "visa",
            "site_num": "5",
            "tenant": "visa",
        },
        {
            "name": "Intuit",
            "subdomain": "intuit",
            "site_num": "5",
            "tenant": "careers",
        },
        {
            "name": "Workday",
            "subdomain": "workday",
            "site_num": "5",
            "tenant": "workday",
        },
    ],
    "greenhouse": [
        {"name": "Databricks",     "slug": "databricks"},
        {"name": "Discord",        "slug": "discord"},
        {"name": "Instawork",      "slug": "instawork"},
        {"name": "GoodLeap",       "slug": "goodleap"},
        {"name": "Okta",           "slug": "okta"},
        {"name": "CrowdStrike",    "slug": "crowdstrike"},
        {"name": "Samsara",        "slug": "samsara"},
        {"name": "MongoDB",        "slug": "mongodb"},
        {"name": "Figma",          "slug": "figma"},
        {"name": "Rippling",       "slug": "rippling"},
        {"name": "Scale AI",       "slug": "scaleai"},
    ],
    "lever": [
        {"name": "Stripe",         "slug": "stripe"},
        {"name": "Thumbtack",      "slug": "thumbtack"},
        {"name": "ServiceTitan",   "slug": "servicetitan"},
        {"name": "Carta",          "slug": "carta"},
        {"name": "OpenAI",         "slug": "openai"},
        {"name": "Anthropic",      "slug": "anthropic"},
    ],
}

# ── Search keywords ───────────────────────────────────────────────────────────
# For Workday: send one search per keyword batch
# For Greenhouse/Lever: filter client-side against these
SEARCH_KEYWORDS = [
    "business operations analyst",
    "engineering operations analyst",
    "technical operations analyst",
    "operations analyst",
    "data analyst",
    "data science",
    "AI solutions",
    "business intelligence",
    "analytics",
    "revenue operations",
    "sales operations",
    "gtm operations",
    "AI analyst",
    "business systems analyst",
    "program analyst",
]

# Title keywords — job must match at least one (case-insensitive substring)
TITLE_INCLUDE_KEYWORDS = [
    "analyst",
    "data science",
    "data scientist",
    "operations",
    "analytics",
    "intelligence",
    "AI solutions",
    "AI engineer",
    "implementation",
]

# Title keywords that auto-reject a role (too senior, wrong domain)
TITLE_EXCLUDE_KEYWORDS = [
    "principal",
    "staff",
    "director",
    "vp ",
    "vice president",
    "manager",          # catches "senior manager" but not "management"
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
]

# ── Scoring thresholds ────────────────────────────────────────────────────────
MIN_MATCH_SCORE = 6          # Only email roles scoring 6+/10
MAX_YOE_REQUIRED = 5         # Skip roles explicitly requiring 5+ years
LOOKBACK_DAYS = 7            # Only surface jobs posted within N days

# ── Email settings ────────────────────────────────────────────────────────────
# Set these in your .env file — do not hardcode here
EMAIL_FROM    = ""           # e.g. jaesongu@gmail.com
EMAIL_TO      = ""           # e.g. jaesongu@gmail.com
EMAIL_SUBJECT = "🎯 New Job Matches — {date} ({count} found)"

# ── Resume variant map ────────────────────────────────────────────────────────
# Claude API returns one of these keys; email tells you which file to use
RESUME_VARIANTS = {
    "biz_ops":      "Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx",
    "eng_ops":      "Jason_Gu_Qualcomm_EngineeringOpsAnalyst_Color.docx",
    "data_science": "Jason_Gu_Qualcomm_DataScientist_FinanceAI_Color.docx",
    "ai_solutions": "Jason_Gu_Salesforce_DataAnalyticsSeniorAnalyst_Color.docx",
    "data_analyst": "Jason_Gu_Disney_DataAnalyst_Color.docx",
}
