# Job Hunter — Automated Job Search System

Monitors 20+ company career pages daily, scores matches against your profile
using Claude AI, and emails you a digest with direct apply links and the right resume variant.

---

## What It Does

1. **Scrapes** Greenhouse, Lever, and Workday career pages across your target companies
2. **Filters** by title keywords, recency (≤7 days), and seniority threshold
3. **Scores** each job 1–10 using Claude API against your specific profile and experience
4. **Emails** a clean HTML digest with score, 3 match reasons, concern flag, and direct apply link
5. **Tracks** all seen jobs in SQLite so you never get duplicates

---

## Setup — 15 Minutes

### 1. Clone and install

```bash
git clone https://github.com/YOUR_USERNAME/job-hunter.git
cd job-hunter
pip install -r requirements.txt
```

### 2. Create your `.env` file

```bash
cp .env.example .env
# Then edit .env with your actual credentials
```

**ANTHROPIC_API_KEY**: Get from [console.anthropic.com](https://console.anthropic.com)

**GMAIL_APP_PASSWORD**: 
- Go to Google Account → Security → 2-Step Verification → App Passwords
- Create a new app password for "Mail"
- Paste the 16-character password (no spaces)

### 3. Test locally

```bash
python main.py --dry-run
```

This runs the full pipeline and prints results without sending email.

Test a single company:
```bash
python main.py --dry-run --company qualcomm
python main.py --dry-run --company databricks
```

### 4. Send a real test email

```bash
python main.py
```

### 5. Push to GitHub and set up automation

```bash
git init && git add . && git commit -m "Initial job hunter setup"
git remote add origin https://github.com/YOUR_USERNAME/job-hunter.git
git push -u origin main
```

Then add your secrets in GitHub:
- Go to repo → Settings → Secrets → Actions
- Add: `ANTHROPIC_API_KEY`, `GMAIL_USER`, `GMAIL_APP_PASSWORD`, `EMAIL_TO`

The GitHub Actions workflow runs automatically every weekday at 8 AM PT.
You can also trigger it manually from the Actions tab.

---

## Adding More Companies

Edit `config.py`:

**Greenhouse company:**
```python
{"name": "Notion", "slug": "notion"},
```
Find the slug at: `boards.greenhouse.io/{slug}` — just try the company name lowercased.

**Lever company:**
```python
{"name": "Figma", "slug": "figma"},
```
Find at: `jobs.lever.co/{slug}`

**Workday company:**
```python
{
    "name": "Nvidia",
    "subdomain": "nvidia",
    "site_num": "5",
    "tenant": "nvidia",
},
```
Find `subdomain` and `tenant` from a job URL like:
`https://nvidia.wd5.myworkdayjobs.com/en-US/NVIDIAExternalCareerSite/...`
→ subdomain=`nvidia`, site_num=`5`, tenant=`NVIDIAExternalCareerSite`

---

## Adjusting Match Threshold

In `config.py`:
```python
MIN_MATCH_SCORE = 6      # Increase to 7 for fewer, higher-quality alerts
LOOKBACK_DAYS   = 7      # Reduce to 3 for only very fresh postings
```

---

## Marking a Job as Applied

```python
from database import mark_applied
mark_applied("wd_qualcomm_JOBID")   # job_id is in the DB
```

Or run `sqlite3 jobs.db` and update manually.

---

## Project Structure

```
job_hunter/
├── .github/workflows/daily_search.yml   # GitHub Actions automation
├── config.py          # All settings, companies, Jason's profile
├── database.py        # SQLite state (seen jobs, run log)
├── scrapers.py        # Greenhouse / Lever / Workday fetchers
├── matcher.py         # Claude API scoring
├── emailer.py         # HTML email digest
├── main.py            # Orchestrator — run this
├── requirements.txt
├── .env.example       # Credential template
└── jobs.db            # Auto-created SQLite database
```

---

## Email Preview

Each job in the digest shows:

```
[STRONG MATCH] Qualcomm — Business Operations Analyst
██████████ 9/10
📍 San Diego, CA · Hybrid | 💰 $74,100–$111,100 | 📅 Posted: Today

Why this fits you:
→ S&OP and demand planning maps to your SDG&E forecasting work
→ KPI dashboard ownership = exactly what you built at Helport
→ AI tool exposure explicitly called out — Helport LLM systems are a differentiator

📄 Resume to use: Jason_Gu_Qualcomm_BizOpsAnalyst_Color.docx

[Apply Now →]
```

---

## Cost Estimate

Claude API scoring: ~$0.05–0.15/day (5–20 jobs × 2K tokens each at Sonnet pricing)
Total monthly: ~$2–4

GitHub Actions: Free (2,000 minutes/month on free tier; this uses ~3 minutes/day)
