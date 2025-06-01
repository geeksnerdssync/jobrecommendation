from fastapi import APIRouter, UploadFile, File, HTTPException
from typing import List
import shutil
import os
from bson import ObjectId

from resume_parser import extract_text_from_pdf, extract_skills
from database import MongoDB
from matcher import match_jobs

router = APIRouter()
db = MongoDB()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def convert_objectid_to_str(obj):
    if isinstance(obj, list):
        return [convert_objectid_to_str(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_objectid_to_str(v) for k, v in obj.items()}
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj

@router.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)
    return {"filename": file.filename, "extracted_skills": skills}

@router.post("/recommend_jobs/")
async def recommend_jobs(skills: List[str]):
    jobs_collection = db.get_collection("jobs")
    jobs = list(jobs_collection.find({}))
    matched = match_jobs(skills, jobs)
    matched_serializable = convert_objectid_to_str(matched)
    return {"matched_jobs": matched_serializable}

@router.get("/debug_jobs/")
async def debug_jobs():
    jobs_collection = db.get_collection("jobs")
    jobs = list(jobs_collection.find({}).limit(10))
    jobs_serializable = convert_objectid_to_str(jobs)
    return {"jobs": jobs_serializable}
