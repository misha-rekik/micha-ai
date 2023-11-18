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

