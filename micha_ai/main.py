from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time

app = FastAPI()

# Enable CORS for all origins, all methods, all headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # This allows all methods
    allow_headers=["*"],  # This allows all headers
)

app.mount("/video", StaticFiles(directory="video"), name="static")

@app.post("/generate_video")
async def generate_video():
    # Simulating a time-consuming task
    time.sleep(5)

    # In a real scenario, you would generate the video and provide the URL
    video_url = "http://localhost:8000/video/video.mp4"
    
    return {"url": video_url}
