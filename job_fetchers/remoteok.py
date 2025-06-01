import requests
from typing import List, Dict
import logging

REMOTEOK_API_URL = "https://remoteok.com/api"

logger = logging.getLogger(__name__)

def fetch_remoteok_jobs() -> List[Dict]:
    try:
        response = requests.get(REMOTEOK_API_URL, headers={"User-Agent": "JobRecommendationBot/1.0"})
        response.raise_for_status()
        data = response.json()
        # The first element is metadata, jobs start from index 1
        jobs = data[1:] if isinstance(data, list) else []
        logger.info(f"Fetched {len(jobs)} jobs from Remote OK")
        return jobs
    except Exception as e:
        logger.error(f"Error fetching Remote OK jobs: {e}")
        return []
