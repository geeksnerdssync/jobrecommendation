from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import router as api_router

app = FastAPI(title="Job Recommendation Backend")

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://jobrecommendation-l8lz.onrender.com", "https://jobrecommendation-1.onrender.com"],  # React dev server origin and deployed frontend URLs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Job Recommendation Backend is running."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
