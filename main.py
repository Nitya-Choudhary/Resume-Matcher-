from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from ml.match import match_resume_to_job

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatchRequest(BaseModel):
    resume: str
    jobDesc: str

@app.post("/api/match")
def match(req: MatchRequest):
    matches = match_resume_to_job(req.resume, req.jobDesc)
    return {"matches": matches}
