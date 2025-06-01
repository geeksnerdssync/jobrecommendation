import os
from pymongo import MongoClient
from pymongo.collection import Collection
from typing import Optional

class MongoDB:
    def __init__(self):
        # Use MongoDB Atlas URI from environment variable or fallback to provided connection string
        uri = os.getenv("MONGODB_URI", "mongodb+srv://ayansy45:T5uA7rwISsY76GOg@apcoerjobsrecommendatio.q3zgtqy.mongodb.net/?retryWrites=true&w=majority&appName=ApcoerJobsRecommendation")
        db_name = os.getenv("MONGODB_DB_NAME", "job_recommendation")
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, name: str) -> Collection:
        return self.db[name]

    def insert_job(self, job_data: dict, collection_name: str = "jobs") -> Optional[str]:
        collection = self.get_collection(collection_name)
        result = collection.update_one(
            {"job_url": job_data.get("job_url")},
            {"$set": job_data},
            upsert=True
        )
        if result.upserted_id:
            return str(result.upserted_id)
        return None
