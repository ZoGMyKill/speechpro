from fastapi import FastAPI, File, UploadFile, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()


# Models for inputs and outputs
class ReportRequest(BaseModel):
    api_key: str
    transcription: str


@app.post("/process_video/")
def process_video(file: UploadFile = File(...)):
    try:
        # Send video to transcription module
        transcription_response = requests.post(
            "http://transcription:8000/transcribe", files={"file": file.file}
        )
        transcription_data = transcription_response.json()

        # Send video to emotion analysis module
        emotion_response = requests.post(
            "http://emotion_analysis:8000/analyze", files={"file": file.file}
        )
        emotion_data = emotion_response.json()

        return {
            "transcription": transcription_data,
            "emotions": emotion_data,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/generate_report/")
def generate_report(request: ReportRequest):
    try:
        # Call report module
        response = requests.post(
            "http://report:8000/generate_report",
            json={"api_key": request.api_key, "transcription": request.transcription},
        )
        return response.json()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
