import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from job_fetchers.remoteok import fetch_remoteok_jobs
from job_fetchers.remotive import fetch_remotive_jobs
from job_fetchers.weworkremotely import fetch_weworkremotely_jobs
from normalization import normalize_remoteok_job, normalize_remotive_job, normalize_weworkremotely_job
from database import MongoDB

logger = logging.getLogger(__name__)
db = MongoDB()

def fetch_and_store_jobs():
    logger.info("Fetching jobs from Remote OK...")
    remoteok_jobs = fetch_remoteok_jobs()
    for job in remoteok_jobs:
        normalized = normalize_remoteok_job(job)
        db.insert_job(normalized)
    logger.info(f"Stored {len(remoteok_jobs)} jobs from Remote OK")

    logger.info("Fetching jobs from Remotive...")
    remotive_jobs = fetch_remotive_jobs()
    for job in remotive_jobs:
        normalized = normalize_remotive_job(job)
        db.insert_job(normalized)
    logger.info(f"Stored {len(remotive_jobs)} jobs from Remotive")

    logger.info("Fetching jobs from We Work Remotely...")
    wework_jobs = fetch_weworkremotely_jobs()
    for job in wework_jobs:
        normalized = normalize_weworkremotely_job(job)
        db.insert_job(normalized)
    logger.info(f"Stored {len(wework_jobs)} jobs from We Work Remotely")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_jobs, 'interval', hours=6)
    scheduler.start()
    logger.info("Scheduler started. Fetching jobs every 6 hours.")

if __name__ == "__main__":
    # For initial testing, run fetch_and_store_jobs once and exit
    fetch_and_store_jobs()
    print("Job fetching completed. Exiting.")
