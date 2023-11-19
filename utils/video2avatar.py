from moviepy.editor import VideoFileClip

import requests
import json
import requests
from requests.auth import HTTPBasicAuth
import json
import time


from google.cloud import storage
from google.oauth2 import service_account
import datetime



####### extract audio from full video
def extract_audio(video_path): 
    
    # Load the video file
    video = VideoFileClip(video_path)

    # Extract the audio from the video
    audio = video.audio

    # Specify the output audio file path
    audio_output_path = 'output_audio.mp3'

    # Write the audio to a new file (you can choose a different format if needed)
    audio.write_audiofile(audio_output_path)

    # Close the video and audio objects
    video.close()
    audio.close()


video_path = '/home/mahdi/__temp__.mp4'


########### storing audio file in google 

def upload_to_gcs_and_get_signed_url(local_file_path, bucket_name, blob_name, json_credentials_path):
    # Authenticate with the JSON credentials file
    credentials = service_account.Credentials.from_service_account_file(json_credentials_path)
    client = storage.Client(credentials=credentials, project=credentials.project_id)

    # Get the bucket object
    bucket = client.bucket(bucket_name)

    # Create a new blob and upload the file
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_file_path)

    # Generate a signed URL valid for 365 days
    url = blob.generate_signed_url(expiration=datetime.timedelta(days=365))

    return url

local_file_path = '/home/mahdi/output_audio.mp3'
bucket_name = 'hackatum23bucket'
blob_name = 'output_audio.mp3'
json_credentials_path = '/home/mahdi/hackatum23/assistant-3712-fd3ad7d8e249.json'

# Upload the file and get the URL
audio_file_url = upload_to_gcs_and_get_signed_url(local_file_path, bucket_name, blob_name, json_credentials_path)
print(audio_file_url)



############### 

# The API endpoint for creating an avatar clip.
api_endpoint = 'https://api.d-id.com/clips'

# API credentials
api_username = 'Y2hhdGdwdG1ha2VhdGhvbkBnbWFpbC5jb20'
api_password = 'HJo9PxUrYDd2hY2AUDnlC'

# The payload with the script, presenter, driver, and background configuration.
payload = {
    "script": {
        "type": "audio",
        "audio_url": audio_file_url
    },
    "presenter_id": "jack-KVaDW71ltd",  # You can choose a different presenter if you wish
    "driver_id": "RISWj5PLjy",         # You can choose a different driver if you wish
    "config": {
        "result_format": "webm"
    },
    "background": {
        "color": False
    }
}

# Make the POST request to create the clip.
response = requests.post(api_endpoint, auth=HTTPBasicAuth(api_username, api_password), json=payload)

clip_data = response.json()
clip_id = clip_data.get("id", "")

####### create a webm out of the avatar clip 

url = "https://api.d-id.com/clips/{clip_id}"

headers = {
    "accept": "application/json",
    "authorization": "Basic WTJoaGRHZHdkRzFoYTJWaGRHaHZia0JuYldGcGJDNWpiMjA6SEpvOVB4VXJZRGQyaFkyQVVEbmxD"
}

response = requests.get(url, headers=headers)

result_data = response.json()

# Access and print the "result_url"
result_url = result_data.get("result_url", "")
print("Result URL:", result_url)
