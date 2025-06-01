from typing import Dict, Any

def normalize_remoteok_job(job: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize a single job from Remote OK API to the common schema.
    Common schema fields:
    - job_title
    - company
    - location
    - skills
    - posted_date
    - job_url
    """
    normalized = {
        "job_title": job.get("position"),
        "company": job.get("company"),
        "location": job.get("location"),
        "skills": job.get("tags", []),
        "posted_date": job.get("date"),
        "job_url": job.get("url"),
        "source": "remoteok"
    }
    return normalized

def normalize_remotive_job(job: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize a single job from Remotive API to the common schema.
    """
    normalized = {
        "job_title": job.get("title"),
        "company": job.get("company_name"),
        "location": job.get("candidate_required_location"),
        "skills": job.get("tags", []),
        "posted_date": job.get("publication_date"),
        "job_url": job.get("url"),
        "source": "remotive"
    }
    return normalized

def normalize_weworkremotely_job(job: Dict[str, Any]) -> Dict[str, Any]:
    """
    Normalize a single job from We Work Remotely crawler to the common schema.
    """
    normalized = {
        "job_title": job.get("job_title"),
        "company": job.get("company"),
        "location": job.get("location"),
        "skills": [],  # No tags available from crawler, can be parsed later if needed
        "posted_date": None,
        "job_url": job.get("job_url"),
        "source": "weworkremotely"
    }
    return normalized
