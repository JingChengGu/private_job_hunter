"""
Job Hunter Configuration — Jason Gu v9
~200 companies across tech, finance, healthcare, media, defense,
e-commerce, logistics, energy, and more. CA + NY focus.
"""

JASON_PROFILE = """
CANDIDATE: Jason Gu | B.S. Data Science, UC San Diego | U.S. Citizen
CURRENT: AI Solutions Engineer @ Helport AI (July 2025-Present)
- Built LLM-powered agent workflow systems, managed 50+ agents, 10+ SMB clients
- Built KPI dashboards, ETL pipelines, cross-functional ops across 3 countries
PRIOR: Data Science Fellow @ SDG&E | Data Science Intern @ Mercury Alert AI
       Data Analyst Intern @ Redrock Biometrics
SKILLS: Python, SQL, PyTorch, Pandas, Scikit-Learn, XGBoost, Tableau, Power BI,
        Airflow, Docker, AWS, LLM Integration, AI Agents, Prompt Engineering, ETL
TARGET: ML Engineer, Applied AI Engineer, AI Solutions Engineer,
        Forward Deployed Engineer, MLOps Engineer, Data Analyst, Ops Analyst
LOCATION: California and New York only (no other states)
"""

TARGET_COMPANIES = {

    # ── GREENHOUSE ────────────────────────────────────────────────────────────
    "greenhouse": [

        # AI / ML platforms
        {"name": "Databricks",          "slug": "databricks"},
        {"name": "Weights & Biases",     "slug": "wandb"},
        {"name": "Glean",               "slug": "glean"},
        {"name": "Moveworks",           "slug": "moveworks"},
        {"name": "Perplexity AI",       "slug": "perplexityai"},
        {"name": "Cohere",              "slug": "cohere"},
        {"name": "Harvey AI",           "slug": "harvey"},
        {"name": "Anduril",             "slug": "anduril"},
        {"name": "Shield AI",           "slug": "shieldai"},
        {"name": "Vannevar Labs",       "slug": "vannevarlabs"},
        {"name": "Covariant",           "slug": "covariant"},
        {"name": "Nuro",                "slug": "nuro"},
        {"name": "Zipline",             "slug": "zipline"},
        {"name": "Kitware",             "slug": "kitware"},
        {"name": "Arize AI",            "slug": "arizeai"},
        {"name": "Pinecone",            "slug": "pinecone"},
        {"name": "Baseten",             "slug": "baseten"},
        {"name": "Modal Labs",          "slug": "modal"},

        # FDE / AI solutions focus (Bay Area) — added after research
        {"name": "xAI",                 "slug": "xai"},
        {"name": "Instabase",           "slug": "instabase"},
        {"name": "Labelbox",            "slug": "labelbox"},
        {"name": "Invisible Technologies", "slug": "invisibletech"},
        {"name": "Aisera",              "slug": "aiserajobs"},
        {"name": "Observe.AI",          "slug": "observeai"},
        {"name": "Vectara",             "slug": "vectara"},

        # Data infrastructure
        {"name": "dbt Labs",            "slug": "dbtlabs"},
        {"name": "Airbyte",             "slug": "airbyte"},
        {"name": "Fivetran",            "slug": "fivetran"},
        {"name": "Hightouch",           "slug": "hightouch"},
        {"name": "Census",              "slug": "census"},
        {"name": "Monte Carlo",         "slug": "montecarlodata"},
        {"name": "Starburst",           "slug": "starburst"},
        {"name": "Cockroach Labs",      "slug": "cockroachlabs"},
        {"name": "SingleStore",         "slug": "singlestore"},

        # Fintech / payments (CA + NY)
        {"name": "Brex",                "slug": "brex"},
        {"name": "Ramp",                "slug": "ramp"},
        {"name": "Chime",               "slug": "chime"},
        {"name": "NerdWallet",          "slug": "nerdwallet"},
        {"name": "Acorns",              "slug": "acorns"},
        {"name": "Plaid",               "slug": "plaid"},
        {"name": "Marqeta",             "slug": "marqeta"},
        {"name": "Upgrade",             "slug": "upgrade"},
        {"name": "Blend",               "slug": "blendlabs"},
        {"name": "Better.com",          "slug": "better"},
        {"name": "Gemini",              "slug": "gemini"},
        {"name": "Robinhood",           "slug": "robinhood"},

        # SaaS / enterprise software
        {"name": "Rippling",            "slug": "rippling"},
        {"name": "Brex",                "slug": "brex"},
        {"name": "Lattice",             "slug": "lattice"},
        {"name": "Gusto",               "slug": "gusto"},
        {"name": "Retool",              "slug": "retool"},
        {"name": "Airtable",            "slug": "airtable"},
        {"name": "Notion",              "slug": "notion"},
        {"name": "Figma",               "slug": "figma"},
        {"name": "Loom",                "slug": "loom"},
        {"name": "Linear",              "slug": "linear"},
        {"name": "Vercel",              "slug": "vercel"},
        {"name": "Replit",              "slug": "replit"},
        {"name": "Sourcegraph",         "slug": "sourcegraph"},
        {"name": "Temporal",            "slug": "temporal"},
        {"name": "Ironclad",            "slug": "ironclad"},
        {"name": "Braze",               "slug": "braze"},
        {"name": "Amplitude",           "slug": "amplitude"},
        {"name": "Mixpanel",            "slug": "mixpanel"},
        {"name": "Yext",                "slug": "yext"},
        {"name": "Squarespace",         "slug": "squarespace"},
        {"name": "Etsy",                "slug": "etsy"},
        {"name": "ZipRecruiter",        "slug": "ziprecruiter"},
        {"name": "Pendo",               "slug": "pendo"},
        {"name": "Grafana Labs",        "slug": "grafana"},
        {"name": "PagerDuty",           "slug": "pagerduty"},
        {"name": "Elastic",             "slug": "elastic"},
        {"name": "HashiCorp",           "slug": "hashicorp"},
        {"name": "Datadog",             "slug": "datadog"},
        {"name": "New Relic",           "slug": "newrelic"},
        {"name": "Cloudflare",          "slug": "cloudflare"},
        {"name": "SentinelOne",         "slug": "sentinelone"},

        # Healthtech / biotech
        {"name": "Oura",                "slug": "ouraring"},
        {"name": "Hims & Hers",         "slug": "forhims"},
        {"name": "Oscar Health",        "slug": "oscar"},
        {"name": "Collective Health",   "slug": "collectivehealth"},
        {"name": "Accolade",            "slug": "accolade"},
        {"name": "Benchling",           "slug": "benchling"},
        {"name": "Veracyte",            "slug": "veracyte"},
        {"name": "Terray Therapeutics", "slug": "terraytherapeutics"},
        {"name": "Insitro",             "slug": "insitro"},
        {"name": "Recursion",           "slug": "recursionpharma"},
        {"name": "Notable Health",      "slug": "notablehealth"},
        {"name": "Suki AI",             "slug": "suki"},
        {"name": "Viz.ai",              "slug": "vizai"},
        {"name": "Commure",             "slug": "commure"},

        # Defense / aerospace
        {"name": "Relativity Space",    "slug": "relativityspace"},
        {"name": "Joby Aviation",       "slug": "jobyaviation"},
        {"name": "Hermeus",             "slug": "hermeus"},
        {"name": "Sift",                "slug": "siftscience"},

        # Media / entertainment
        {"name": "Spotify",             "slug": "spotify"},
        {"name": "SoundCloud",          "slug": "soundcloud"},
        {"name": "Vimeo",               "slug": "vimeo"},
        {"name": "Peloton",             "slug": "pelotoncycle"},
        {"name": "Headspace",           "slug": "headspace"},

        # E-commerce / marketplace
        {"name": "Instacart",           "slug": "instacart"},
        {"name": "DoorDash",            "slug": "doordash"},
        {"name": "Grubhub",             "slug": "grubhub"},
        {"name": "OpenTable",           "slug": "opentable"},
        {"name": "Yelp",                "slug": "yelp"},
        {"name": "Poshmark",            "slug": "poshmark"},
        {"name": "Whatnot",             "slug": "whatnot"},
        {"name": "Faire",               "slug": "faire"},

        # Real estate / proptech
        {"name": "Compass",             "slug": "compass"},
        {"name": "Opendoor",            "slug": "opendoor"},
        {"name": "Redfin",              "slug": "redfin"},
        {"name": "Zeus Living",         "slug": "zeusliving"},

        # Edtech
        {"name": "Coursera",            "slug": "coursera"},
        {"name": "Duolingo",            "slug": "duolingo"},
        {"name": "Chegg",               "slug": "chegg"},
        {"name": "Lambda School",       "slug": "lambdaschool"},
        {"name": "Outlier AI",          "slug": "outlierai"},

        # Logistics / supply chain
        {"name": "Flexport",            "slug": "flexport"},
        {"name": "project44",           "slug": "project44"},

        # SD domain companies
        {"name": "Vannevar Labs",       "slug": "vannevarlabs"},
        {"name": "Samsara",             "slug": "samsara"},
        {"name": "Discord",             "slug": "discord"},
        {"name": "Okta",                "slug": "okta"},
        {"name": "CrowdStrike",         "slug": "crowdstrike"},
        {"name": "MongoDB",             "slug": "mongodb"},
        {"name": "Instawork",           "slug": "instawork"},
        {"name": "GoodLeap",            "slug": "goodleap"},
    ],

    # ── LEVER ─────────────────────────────────────────────────────────────────
    "lever": [
        {"name": "Stripe",              "slug": "stripe"},
        {"name": "OpenAI",              "slug": "openai"},
        {"name": "Anthropic",           "slug": "anthropic"},
        {"name": "Character AI",        "slug": "characterai"},
        {"name": "Mistral AI",          "slug": "mistral"},
        {"name": "Inflection AI",       "slug": "inflection"},
        {"name": "Luma AI",             "slug": "lumalabs"},
        {"name": "Runway",              "slug": "runwayml"},
        {"name": "Carta",               "slug": "carta"},
        {"name": "ServiceTitan",        "slug": "servicetitan"},
        {"name": "Thumbtack",           "slug": "thumbtack"},
        {"name": "Viasat",              "slug": "viasat"},
        {"name": "Shield AI",           "slug": "shieldai"},
        {"name": "Vannevar Labs",       "slug": "vannevarlabs-2"},
        {"name": "Neuralmagic",         "slug": "neuralmagic"},
        {"name": "Syntiant",            "slug": "syntiant"},
        {"name": "Prefect",             "slug": "prefect"},
        {"name": "SoFi",                "slug": "sofi"},
        {"name": "Coinbase",            "slug": "coinbase"},
        {"name": "Kraken",              "slug": "kraken"},
        {"name": "Figma",               "slug": "figma"},
        {"name": "Notion",              "slug": "notion"},
        {"name": "Scale AI",            "slug": "scaleai"},
        {"name": "Palantir",            "slug": "palantir"},
        {"name": "Navan",               "slug": "navan"},
        {"name": "Pipe",                "slug": "pipe"},
        {"name": "Faire",               "slug": "faire"},
        {"name": "Mercury",             "slug": "mercury"},
        {"name": "Deel",                "slug": "deel"},
        {"name": "Remote.com",          "slug": "remote"},
        {"name": "Ripple",              "slug": "ripple"},
        {"name": "Gemini Crypto",       "slug": "gemini"},
        {"name": "Pilot.com",           "slug": "pilot"},
        {"name": "Attentive",           "slug": "attentive"},
        {"name": "Qualified",           "slug": "qualified"},
        {"name": "Gong",                "slug": "gong"},
        {"name": "Outreach",            "slug": "outreach"},
        {"name": "Salesloft",           "slug": "salesloft"},
        {"name": "HackerOne",           "slug": "hackerone"},
        {"name": "Abnormal Security",   "slug": "abnormalsecurity"},
        {"name": "Lacework",            "slug": "lacework"},

        # FDE / AI solutions focus (Bay Area) — added after research
        {"name": "Hive AI",             "slug": "hive"},
        {"name": "Encord",              "slug": "CordTechnologies"},
        {"name": "Aircall",             "slug": "aircall"},
        {"name": "Agiloft",             "slug": "agiloft"},
    ],

    # ── WORKDAY ───────────────────────────────────────────────────────────────
    # Only verified or high-confidence tenants
    "workday": [

        # Big tech (CA)
        {"name": "Qualcomm",            "subdomain": "qualcomm",          "site_num": "5",  "tenant": "qualcomm_career"},
        {"name": "Salesforce",          "subdomain": "salesforce",        "site_num": "12", "tenant": "External_Career_Site"},
        {"name": "Adobe",               "subdomain": "adobe",             "site_num": "5",  "tenant": "external_corporate"},
        {"name": "Nvidia",              "subdomain": "nvidia",            "site_num": "5",  "tenant": "NVIDIAExternalCareerSite"},
        {"name": "Cisco",               "subdomain": "cisco",             "site_num": "5",  "tenant": "Cisco"},
        {"name": "Snowflake",           "subdomain": "snowflake",         "site_num": "5",  "tenant": "Snowflake"},
        {"name": "ServiceNow",          "subdomain": "servicenow",        "site_num": "5",  "tenant": "servicenow"},
        {"name": "Intuit",              "subdomain": "intuit",            "site_num": "5",  "tenant": "careers"},
        {"name": "Palo Alto Networks",  "subdomain": "paloaltonetworks",  "site_num": "1",  "tenant": "PaloAltoNetworks"},
        {"name": "Splunk",              "subdomain": "splunk",            "site_num": "5",  "tenant": "splunk"},
        {"name": "Zendesk",             "subdomain": "zendesk",           "site_num": "5",  "tenant": "zendesk"},
        {"name": "Atlassian",           "subdomain": "atlassian",         "site_num": "5",  "tenant": "atlassian"},
        {"name": "Workday",             "subdomain": "workday",           "site_num": "5",  "tenant": "workday"},
        {"name": "Box",                 "subdomain": "box",               "site_num": "5",  "tenant": "boxexternalcareers"},
        {"name": "Dropbox",             "subdomain": "dropbox",           "site_num": "5",  "tenant": "Dropbox"},
        {"name": "Twilio",              "subdomain": "twilio",            "site_num": "5",  "tenant": "twilio"},
        {"name": "Pinterest",           "subdomain": "pinterest",         "site_num": "5",  "tenant": "pinterest"},
        {"name": "Lyft",                "subdomain": "lyft",              "site_num": "5",  "tenant": "lyft"},
        {"name": "Airbnb",              "subdomain": "airbnb",            "site_num": "5",  "tenant": "Airbnb"},
        {"name": "Uber",                "subdomain": "uber",              "site_num": "5",  "tenant": "uberats"},

        # Finance / banking (CA + NY)
        {"name": "Capital One",         "subdomain": "capitalone",        "site_num": "5",  "tenant": "Capital_One"},
        {"name": "American Express",    "subdomain": "aexp",              "site_num": "5",  "tenant": "aexp"},
        {"name": "Mastercard",          "subdomain": "mastercard",        "site_num": "5",  "tenant": "mastercard"},
        {"name": "PayPal",              "subdomain": "paypal",            "site_num": "5",  "tenant": "paypal"},
        {"name": "Visa",                "subdomain": "visa",              "site_num": "5",  "tenant": "visa"},
        {"name": "Fidelity",            "subdomain": "fidelity",          "site_num": "5",  "tenant": "fidelity"},
        {"name": "BlackRock",           "subdomain": "blackrock",         "site_num": "5",  "tenant": "blackrock"},
        {"name": "JPMorgan Chase",      "subdomain": "jpmc",              "site_num": "5",  "tenant": "jpmchase"},
        {"name": "Goldman Sachs",       "subdomain": "goldmansachs",      "site_num": "5",  "tenant": "Goldman_Sachs_Careers"},
        {"name": "Morgan Stanley",      "subdomain": "morganstanley",     "site_num": "5",  "tenant": "morganstanley"},
        {"name": "Bloomberg",           "subdomain": "bloomberg",         "site_num": "5",  "tenant": "Bloomberg"},
        {"name": "The Trade Desk",      "subdomain": "thetradedesk",      "site_num": "5",  "tenant": "ExternalCareerSite"},

        # Healthcare / medical (CA)
        {"name": "ResMed",              "subdomain": "resmed",            "site_num": "3",  "tenant": "ResMed_External_Careers"},
        {"name": "Dexcom",              "subdomain": "dexcom",            "site_num": "1",  "tenant": "Dexcom"},
        {"name": "Tandem Diabetes",     "subdomain": "tandemdiabetes",    "site_num": "12", "tenant": "tandemdiabetes"},
        {"name": "Illumina",            "subdomain": "illumina",          "site_num": "5",  "tenant": "illumina"},
        {"name": "Intuitive Surgical",  "subdomain": "intuitive",         "site_num": "5",  "tenant": "intuitive"},
        {"name": "Edwards Lifesciences","subdomain": "edwards",           "site_num": "5",  "tenant": "Edwards_Lifesciences"},
        {"name": "Boston Scientific",   "subdomain": "bostonscientific",  "site_num": "5",  "tenant": "bostonscientific"},
        {"name": "Hologic",             "subdomain": "hologic",           "site_num": "5",  "tenant": "hologic"},
        {"name": "Becton Dickinson",    "subdomain": "bd",                "site_num": "5",  "tenant": "bd"},
        {"name": "Genentech",           "subdomain": "gene",              "site_num": "5",  "tenant": "gene"},
        {"name": "Gilead Sciences",     "subdomain": "gilead",            "site_num": "5",  "tenant": "gilead"},
        {"name": "Exact Sciences",      "subdomain": "exactsciences",     "site_num": "5",  "tenant": "exactsciences"},
        {"name": "Pacific Biosciences", "subdomain": "pacbio",            "site_num": "5",  "tenant": "pacbio"},

        # Defense / aerospace (CA)
        {"name": "Leidos",              "subdomain": "leidos",            "site_num": "5",  "tenant": "leidos"},
        {"name": "Booz Allen Hamilton", "subdomain": "bah",               "site_num": "5",  "tenant": "bah"},
        {"name": "SAIC",                "subdomain": "saic",              "site_num": "5",  "tenant": "saic"},
        {"name": "Northrop Grumman",    "subdomain": "northropgrumman",   "site_num": "5",  "tenant": "northropgrumman"},
        {"name": "L3Harris",            "subdomain": "l3harris",          "site_num": "5",  "tenant": "l3harris"},
        {"name": "Cubic",               "subdomain": "cubic",             "site_num": "5",  "tenant": "cubic"},

        # Media / entertainment (CA + NY)
        {"name": "Disney",              "subdomain": "disney",            "site_num": "5",  "tenant": "disneycareer"},
        {"name": "NBCUniversal",        "subdomain": "nbcunicareers",     "site_num": "5",  "tenant": "NBCUniversal"},
        {"name": "Warner Bros Discovery","subdomain": "warnermedia",      "site_num": "5",  "tenant": "warnermedia"},
        {"name": "Paramount",           "subdomain": "paramount",         "site_num": "5",  "tenant": "paramount"},
        {"name": "Sony Pictures",       "subdomain": "sonypictures",      "site_num": "5",  "tenant": "sonypictures"},
        {"name": "Electronic Arts",     "subdomain": "ea",                "site_num": "5",  "tenant": "EA"},

        # Telecom / hardware (CA)
        {"name": "Verizon",             "subdomain": "verizon",           "site_num": "5",  "tenant": "verizon"},
        {"name": "T-Mobile",            "subdomain": "tmobile",           "site_num": "5",  "tenant": "tmobile"},
        {"name": "Intel",               "subdomain": "intel",             "site_num": "5",  "tenant": "intel"},
        {"name": "Broadcom",            "subdomain": "broadcom",          "site_num": "5",  "tenant": "broadcom"},
        {"name": "Western Digital",     "subdomain": "westerndigital",    "site_num": "5",  "tenant": "westerndigital"},
        {"name": "Pure Storage",        "subdomain": "purestorage",       "site_num": "5",  "tenant": "purestorage"},

        # Energy / cleantech (CA)
        {"name": "Enphase Energy",      "subdomain": "enphase",           "site_num": "5",  "tenant": "enphase"},
        {"name": "SunPower",            "subdomain": "sunpower",          "site_num": "5",  "tenant": "sunpower"},
        {"name": "ChargePoint",         "subdomain": "chargepoint",       "site_num": "5",  "tenant": "chargepoint"},
        {"name": "Stem Inc",            "subdomain": "stem",              "site_num": "5",  "tenant": "stem"},

        # Consulting / professional services
        {"name": "Accenture",           "subdomain": "accenture",         "site_num": "5",  "tenant": "accenture"},
        {"name": "Deloitte",            "subdomain": "deloitte",          "site_num": "5",  "tenant": "deloitte"},
        {"name": "KPMG",                "subdomain": "kpmg",              "site_num": "5",  "tenant": "kpmgcareers"},
        {"name": "EY",                  "subdomain": "ey",                "site_num": "5",  "tenant": "EY"},
        {"name": "PwC",                 "subdomain": "pwc",               "site_num": "5",  "tenant": "gx"},
        {"name": "IBM",                 "subdomain": "ibm",               "site_num": "5",  "tenant": "ibm"},

        # Logistics / supply chain (CA)
        {"name": "XPO Logistics",       "subdomain": "xpo",               "site_num": "5",  "tenant": "xpo"},
        {"name": "FedEx",               "subdomain": "fedex",             "site_num": "5",  "tenant": "fedex"},

        # Real estate / proptech (CA + NY)
        {"name": "CBRE",                "subdomain": "cbre",              "site_num": "5",  "tenant": "cbre"},
        {"name": "Jones Lang LaSalle",  "subdomain": "jll",               "site_num": "5",  "tenant": "jll"},
        {"name": "Zillow",              "subdomain": "zillow",            "site_num": "5",  "tenant": "zillow"},
        {"name": "CoStar",              "subdomain": "costar",            "site_num": "5",  "tenant": "costar"},

        # Retail / e-commerce (CA + NY)
        {"name": "Gap Inc",             "subdomain": "gapinc",            "site_num": "5",  "tenant": "gap"},
        {"name": "Williams-Sonoma",     "subdomain": "williams-sonomainc","site_num": "5",  "tenant": "williams-sonomainc"},
        {"name": "Chewy",               "subdomain": "chewy",             "site_num": "5",  "tenant": "chewy"},
    ],

    # ── WORKABLE ─────────────────────────────────────────────────────────────
    "workable": [
        {"name": "Alphatec Spine",      "slug": "atec-spine"},
        {"name": "Nuvation Bio",        "slug": "nuvation-bio"},
        {"name": "Artera Health",       "slug": "artera"},
        {"name": "Solv Health",         "slug": "solv"},
    ],
}

# ── Search keywords (Workday) ─────────────────────────────────────────────────
SEARCH_KEYWORDS = [
    "forward deployed engineer",
    "AI solutions engineer",
    "AI sales engineer",
    "AI engineer",
    "machine learning engineer",
    "applied AI",
    "MLOps",
    "operations analyst",
    "data analyst",
    "data scientist",
    "solutions engineer",
    "AI implementation",
    "business operations",
    "analytics engineer",
    "software engineer AI",
    "ML platform",
    "data engineer",
]

# ── Title filters ─────────────────────────────────────────────────────────────
TITLE_INCLUDE_KEYWORDS = [
    "analyst", "data science", "data scientist", "data engineer",
    "operations", "analytics", "ai solutions", "ai engineer",
    "ai implementation", "solutions engineer", "forward deployed",
    "implementation", "machine learning", "ml engineer", "mlops",
    "applied ai", "software engineer",
    "ai sales engineer", "sales engineer",
]

TITLE_EXCLUDE_KEYWORDS = [
    "principal", "staff ", "director", "vp ", "vice president",
    "manager", "head of", "legal", "attorney", "accountant",
    "recruiter", "hardware", "embedded", "firmware", "mechanical",
    "civil", "electrical", "intern", "internship",
    "financial analyst", "finance analyst", "accounting analyst",
    "tax analyst", "treasury analyst",
    "research engineer",
    "research scientist",
    "solutions architect",
    "specialist solutions",
    "creative strategist", "strategist",
    "security sales",
]

# ── Thresholds ────────────────────────────────────────────────────────────────
MIN_MATCH_SCORE      = 7
MAX_YOE_REQUIRED     = 5
LOOKBACK_DAYS        = 9    # 9 calendar days = 5 full business days
COMPANY_COOLDOWN_DAYS = 3   # same company won't appear more than once every 3 days

# ── Location scope ────────────────────────────────────────────────────────────
ALLOWED_STATES = ["california", "new york"]  # Only CA and NY per user preference

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
