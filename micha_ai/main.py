from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from celery import Celery
from pathlib import Path
import time

app = FastAPI()


celery = Celery(__name__, broker="pyamqp://guest:guest@localhost//")

@celery.task
def generate_video(book_title: str, video_type: str):
    time.sleep(300)  # Mock video generation
    return f"Generated video for '{book_title}' of type '{video_type}'"

# Callback function to send the video to the frontend
def send_video_to_user(task_id: str):
    result = generate_video.AsyncResult(task_id)
    video_url = result.get()
    print(f"Video generated: {video_url}")
    
    
# Endpoint to initiate video generation
@app.post("/generate_video")
async def generate_video_endpoint(
    book_title: str, video_type: str, background_tasks: BackgroundTasks
):
    task = generate_video.delay(book_title, video_type)
    background_tasks.add_task(send_video_to_user, task.id)

    return {"message": f"Video generation for '{book_title}' started. Check back later."}


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

