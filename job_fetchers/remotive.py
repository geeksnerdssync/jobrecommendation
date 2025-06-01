import requests
from typing import List, Dict

REMOTIVE_API_URL = "https://remotive.com/api/remote-jobs"

def fetch_remotive_jobs() -> List[Dict]:
    try:
        response = requests.get(REMOTIVE_API_URL, headers={"User-Agent": "JobRecommendationBot/1.0"})
        response.raise_for_status()
        data = response.json()
        jobs = data.get("jobs", [])
        return jobs
    except Exception as e:
        print(f"Error fetching Remotive jobs: {e}")
        return []
