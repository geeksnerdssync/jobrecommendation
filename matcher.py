from typing import List, Dict
from sentence_transformers import SentenceTransformer, util

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def match_jobs(resume_skills: List[str], jobs: List[Dict]) -> List[Dict]:
    """
    Match jobs to resume skills using semantic similarity.
    Returns jobs sorted by similarity score descending.
    Filters jobs to include only those located in India or remote jobs.
    """
    if not resume_skills:
        return []

    resume_text = " ".join(resume_skills)
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)

    matched_jobs = []
    for job in jobs:
        location = job.get("location", "").lower()
        # Filter jobs: include if location contains 'india' or is remote
        if "india" in location or "remote" in location:
            job_skills = job.get("skills", [])
            job_text = " ".join(job_skills)
            job_embedding = model.encode(job_text, convert_to_tensor=True)
            similarity = util.pytorch_cos_sim(resume_embedding, job_embedding).item()
            matched_jobs.append((similarity, job))

    matched_jobs.sort(key=lambda x: x[0], reverse=True)
    return [job for _, job in matched_jobs]
