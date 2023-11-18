from fastapi import FastAPI, BackgroundTasks, UploadFile, File
from celery import Celery
from pathlib import Path
import time
import langchain
from dotenv import load_dotenv
import os
from openai import OpenAI




app = FastAPI()

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


@app.get("/test_openai")
def test_openai_integration(book_title: str):
    # Check if the OpenAI API key is set
    # if OpenAI.api_key is None:
    #     return {"error": "OpenAI API key is not set. Please check your configuration."}
    
    # Create a simple request to OpenAI's GPT-3 model
    try:
        response = client.completions.create(model="gpt-3.5-turbo",
        prompt=f"Summarize the book '{book_title}' in a few sentences.")
        generated_text = response['choices'][0]['message']['content']
        return {"generated_text": generated_text}
    except Exception as e:
        return {"error": str(e)}

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

