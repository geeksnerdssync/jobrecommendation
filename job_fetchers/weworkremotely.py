import requests
from bs4 import BeautifulSoup
from typing import List, Dict
import time

BASE_URL = "https://weworkremotely.com/remote-jobs/search?term=developer"
HEADERS = {"User-Agent": "JobRecommendationBot/1.0"}

def fetch_weworkremotely_jobs() -> List[Dict]:
    jobs = []
    try:
        response = requests.get(BASE_URL, headers=HEADERS)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        job_sections = soup.find_all("section", class_="jobs")
        for section in job_sections:
            job_posts = section.find_all("li", class_=lambda x: x != "view-all")
            for job in job_posts:
                anchor = job.find("a", href=True)
                if anchor:
                    job_url = "https://weworkremotely.com" + anchor['href']
                    company = job.find("span", class_="company")
                    title = job.find("span", class_="title")
                    region = job.find("span", class_="region company")
                    jobs.append({
                        "job_url": job_url,
                        "company": company.text.strip() if company else "",
                        "job_title": title.text.strip() if title else "",
                        "location": region.text.strip() if region else "",
                        "source": "weworkremotely"
                    })
        time.sleep(1)  # polite delay
    except Exception as e:
        print(f"Error fetching We Work Remotely jobs: {e}")
    return jobs
