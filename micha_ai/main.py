from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time
import langchain
from dotenv import load_dotenv
import os
from openai import OpenAI




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
load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


@app.post("/generate_video")
async def generate_video():
    # Simulating a time-consuming task
    time.sleep(5)

@app.get("/test_openai")
def test_openai_integration(book_title: str):

    try:
        response = client.completions.create(model="gpt-3.5-turbo",
        prompt=f"Summarize the book '{book_title}' in a few sentences.")
        generated_text = response['choices'][0]['message']['content']
        return {"generated_text": generated_text}
    except Exception as e:
        return {"error": str(e)}

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

    # In a real scenario, you would generate the video and provide the URL
    video_url = "http://localhost:8000/video/video.mp4"
    
    return {"url": video_url}
