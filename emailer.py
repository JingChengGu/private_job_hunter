"""
emailer.py — Sends the daily job digest via Gmail SMTP

Email structure per job:
  [Score badge] Company — Title
  📍 Location | 💰 Salary | Posted: Date
  Why it matches (3 bullets)
  Resume to use: [variant name]
  [APPLY NOW button]
"""

import os
import smtplib
import logging
from datetime import date
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import EMAIL_FROM, EMAIL_TO, EMAIL_SUBJECT, RESUME_VARIANTS

log = logging.getLogger(__name__)

# ── Score badge colors ────────────────────────────────────────────────────────
def _score_badge(score: int) -> tuple[str, str]:
    """Returns (background_hex, label)"""
    if score >= 9:  return ("#1B3A6B", "STRONG MATCH")
    if score >= 7:  return ("#2563EB", "GOOD MATCH")
    if score >= 6:  return ("#0891B2", "SOLID FIT")
    return              ("#6B7280", "POSSIBLE FIT")


def _score_bar(score: int) -> str:
    """Visual 10-block score bar."""
    filled = "█" * score
    empty  = "░" * (10 - score)
    return f"{filled}{empty}"


def _build_job_block(job: dict) -> str:
    """Render one job as an HTML block."""
    bg, label = _score_badge(job["score"])
    variant_key  = job.get("resume_variant", "biz_ops")
    variant_file = RESUME_VARIANTS.get(variant_key, "See resume variants")
    salary       = job.get("salary") or "Not listed"
    posted       = job.get("posted_date") or "Recently"
    concern      = job.get("concern", "")
    reasons      = job.get("match_reasons", [])

    reasons_html = "".join(
        f'<li style="margin-bottom:6px;">{r}</li>'
        for r in reasons
    )

    concern_html = (
        f'<div style="margin-top:10px;padding:8px 12px;background:#FEF3C7;'
        f'border-left:3px solid #F59E0B;border-radius:4px;font-size:13px;color:#92400E;">'
        f'⚠️  <strong>Watch:</strong> {concern}'
        f'</div>'
    ) if concern and concern.lower() != "none" else ""

    return f"""
<div style="background:#fff;border:1px solid #E5E7EB;border-radius:8px;
            padding:20px 24px;margin-bottom:20px;">

  <!-- Score badge + title -->
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px;">
    <span style="background:{bg};color:#fff;padding:3px 10px;border-radius:4px;
                 font-size:12px;font-weight:700;letter-spacing:.5px;">{label}</span>
    <span style="font-size:18px;font-weight:700;color:#111;">{job["company"]}</span>
    <span style="color:#6B7280;font-size:16px;">— {job["title"]}</span>
  </div>

  <!-- Score bar -->
  <div style="font-family:monospace;font-size:14px;color:{bg};margin-bottom:10px;">
    {_score_bar(job["score"])} {job["score"]}/10
  </div>

  <!-- Meta row -->
  <div style="font-size:13px;color:#6B7280;margin-bottom:14px;">
    📍 {job.get("location","Not specified")} &nbsp;|&nbsp;
    💰 {salary} &nbsp;|&nbsp;
    📅 Posted: {posted}
  </div>

  <!-- Match reasons -->
  <div style="font-size:14px;color:#374151;margin-bottom:10px;">
    <strong>Why this fits you:</strong>
    <ul style="margin:8px 0 0 0;padding-left:20px;">
      {reasons_html}
    </ul>
  </div>

  <!-- Resume variant -->
  <div style="font-size:13px;background:#F0F9FF;border-radius:4px;
              padding:8px 12px;margin-bottom:10px;color:#0C4A6E;">
    📄 <strong>Resume to use:</strong> {variant_file}
  </div>

  {concern_html}

  <!-- Apply button -->
  <div style="margin-top:14px;">
    <a href="{job['url']}"
       style="display:inline-block;background:{bg};color:#fff;padding:10px 20px;
              border-radius:6px;text-decoration:none;font-weight:600;font-size:14px;">
      Apply Now →
    </a>
  </div>

</div>
"""


def build_html_email(jobs: list[dict]) -> str:
    """Assemble full HTML email body."""
    today = date.today().strftime("%B %d, %Y")
    count = len(jobs)

    job_blocks = "".join(_build_job_block(j) for j in jobs)

    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="margin:0;padding:0;background:#F3F4F6;font-family:Arial,sans-serif;">
<div style="max-width:680px;margin:0 auto;padding:20px;">

  <!-- Header -->
  <div style="background:#1B3A6B;border-radius:8px;padding:24px;margin-bottom:20px;text-align:center;">
    <div style="font-size:28px;margin-bottom:4px;">🎯</div>
    <h1 style="color:#fff;margin:0;font-size:20px;font-weight:700;">
      {count} New Job Match{"es" if count != 1 else ""} Found
    </h1>
    <p style="color:#93C5FD;margin:6px 0 0 0;font-size:14px;">{today}</p>
  </div>

  <!-- Tip banner -->
  <div style="background:#ECFDF5;border:1px solid #6EE7B7;border-radius:8px;
              padding:12px 16px;margin-bottom:20px;font-size:13px;color:#065F46;">
    💡 <strong>Tip:</strong> Paste the job description to your Claude conversation
    to get a fully tailored resume in under 2 minutes.
  </div>

  <!-- Job blocks -->
  {job_blocks}

  <!-- Footer -->
  <div style="text-align:center;font-size:12px;color:#9CA3AF;margin-top:24px;padding-top:16px;
              border-top:1px solid #E5E7EB;">
    Job Hunter — Running daily at 8 AM PT
    <br>To pause alerts, disable the GitHub Actions workflow.
  </div>

</div>
</body>
</html>
"""


def send_email(jobs: list[dict], dry_run: bool = False) -> bool:
    """
    Send the digest email via Gmail SMTP.
    Set dry_run=True to print the HTML instead of sending.
    """
    if not jobs:
        log.info("No jobs to email.")
        return True

    today = date.today().strftime("%B %d, %Y")
    subject = EMAIL_SUBJECT.format(date=today, count=len(jobs))
    html_body = build_html_email(jobs)

    if dry_run:
        print("=" * 60)
        print(f"SUBJECT: {subject}")
        print("=" * 60)
        for j in jobs:
            print(f"  [{j['score']}/10] {j['company']} — {j['title']}")
            print(f"  📍 {j.get('location','?')} | 💰 {j.get('salary','?')}")
            for r in j.get("match_reasons", []):
                print(f"  → {r}")
            print(f"  Resume: {RESUME_VARIANTS.get(j.get('resume_variant','biz_ops'))}")
            print(f"  URL: {j['url']}")
            print()
        return True

    # Read credentials from environment
    gmail_user     = os.environ.get("GMAIL_USER", EMAIL_FROM)
    gmail_password = os.environ.get("GMAIL_APP_PASSWORD", "")

    if not gmail_password:
        log.error("GMAIL_APP_PASSWORD not set. Cannot send email.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"]    = gmail_user
    msg["To"]      = os.environ.get("EMAIL_TO", EMAIL_TO)

    # Plain-text fallback
    plain = f"New job matches — {today}\n\n"
    for j in jobs:
        plain += f"[{j['score']}/10] {j['company']} — {j['title']}\n"
        plain += f"  {j.get('location','')} | {j.get('salary','')}\n"
        plain += f"  Apply: {j['url']}\n\n"

    msg.attach(MIMEText(plain, "plain"))
    msg.attach(MIMEText(html_body, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(gmail_user, gmail_password)
            smtp.sendmail(gmail_user, msg["To"], msg.as_string())
        log.info("Email sent to %s (%d jobs)", msg["To"], len(jobs))
        return True
    except Exception as e:
        log.error("Email send failed: %s", e)
        return False
