from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import time
import langchain
from dotenv import load_dotenv
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))




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


@app.post("/generate_video")
async def generate_video():
    # Simulating a time-consuming task
    time.sleep(5)
    narration = get_narration("the little prince")

@app.get("/test_openai")
def get_narration(book_title: str):

    template = (f"We want to generate a trailer for the book {book_title}, we plan to use DALL-E to generate the images for the trailer. Can you please provide us with short sentences for the trailer of the book and for every sentence please provide us with the necessary prompt we can use to generate images for the sentence with DALL-E. Please follow the following format for every sentences pair\n story: xxx\nscene: xxx\nCan you also please only output the specified format, please do not include anything else.")

    messages = [
        {"role": "user",
         "content": template
         },
    ]


    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    reply = completion.choices[0].message.content

    stories_list = []
    scenes_list = []

    sentences = reply.split('\n')
    filtered = list(filter(lambda x: x != '', sentences))

    for sentence in filtered:
        parts = sentence.split(":")
        if parts[0][-1] == 'y':
            stories_list.append(parts[1].strip())
        else:
            scenes_list.append(f"in the style of the book {book_title}, " + parts[1].strip())

    my_dict = {} 
    i=0
    # test_sentence = scenes_list[0]
    for test_sentence in scenes_list:
        response = client.images.generate(model="dall-e-3",prompt=test_sentence,quality="standard",n=1,)
        my_dict[response.data[0].url]= stories_list[i]
        # my_dict[test_sentence]= stories_list[i]
        i=i+1
    # print(my_dict)

    return my_dict

    # response = client.images.generate(
    # model="dall-e-3",
    # prompt=test_sentence,
    # quality="standard",
    # n=1,
    # )

    # image_url = response.data[0].url

    # return image_url

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

    # In a real scenario, you would generate the video and provide the URL
    video_url = "http://localhost:8000/video/video.mp4"
    
    return {"url": video_url}
