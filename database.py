"""
database.py — SQLite state management
Tracks every job seen so you never get duplicate emails.
Stores your application history for reference.
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "jobs.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables if they don't exist. Safe to call on every run."""
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS seen_jobs (
                job_id        TEXT PRIMARY KEY,
                company       TEXT NOT NULL,
                title         TEXT NOT NULL,
                location      TEXT,
                url           TEXT NOT NULL,
                salary        TEXT,
                posted_date   TEXT,
                found_date    TEXT NOT NULL,
                score         INTEGER,
                resume_variant TEXT,
                match_reasons TEXT,
                status        TEXT DEFAULT 'new'
            );

            CREATE TABLE IF NOT EXISTS run_log (
                run_id        INTEGER PRIMARY KEY AUTOINCREMENT,
                run_date      TEXT NOT NULL,
                jobs_fetched  INTEGER DEFAULT 0,
                jobs_new      INTEGER DEFAULT 0,
                jobs_emailed  INTEGER DEFAULT 0,
                errors        TEXT
            );
        """)


def is_seen(job_id: str) -> bool:
    with get_conn() as conn:
        row = conn.execute(
            "SELECT 1 FROM seen_jobs WHERE job_id = ?", (job_id,)
        ).fetchone()
        return row is not None


def save_job(job: dict):
    """Insert a new job. Silently ignores if already exists."""
    with get_conn() as conn:
        conn.execute("""
            INSERT OR IGNORE INTO seen_jobs
                (job_id, company, title, location, url, salary,
                 posted_date, found_date, score, resume_variant, match_reasons, status)
            VALUES
                (:job_id, :company, :title, :location, :url, :salary,
                 :posted_date, :found_date, :score, :resume_variant, :match_reasons, :status)
        """, {
            "job_id":        job["id"],
            "company":       job["company"],
            "title":         job["title"],
            "location":      job.get("location", ""),
            "url":           job["url"],
            "salary":        job.get("salary", ""),
            "posted_date":   job.get("posted_date", ""),
            "found_date":    datetime.utcnow().strftime("%Y-%m-%d"),
            "score":         job.get("score"),
            "resume_variant": job.get("resume_variant", ""),
            "match_reasons": "\n".join(job.get("match_reasons", [])),
            "status":        "new",
        })


def mark_applied(job_id: str):
    """Call this when you've submitted an application."""
    with get_conn() as conn:
        conn.execute(
            "UPDATE seen_jobs SET status = 'applied' WHERE job_id = ?",
            (job_id,)
        )


def log_run(jobs_fetched: int, jobs_new: int, jobs_emailed: int, errors: str = ""):
    with get_conn() as conn:
        conn.execute("""
            INSERT INTO run_log (run_date, jobs_fetched, jobs_new, jobs_emailed, errors)
            VALUES (?, ?, ?, ?, ?)
        """, (datetime.utcnow().strftime("%Y-%m-%d %H:%M"), jobs_fetched, jobs_new, jobs_emailed, errors))


def get_recent_jobs(days: int = 7):
    """Pull recent jobs for review — useful for a weekly summary."""
    with get_conn() as conn:
        return conn.execute("""
            SELECT * FROM seen_jobs
            WHERE found_date >= date('now', ?)
            ORDER BY score DESC, found_date DESC
        """, (f"-{days} days",)).fetchall()
