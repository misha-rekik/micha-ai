from elevenlabs import generate, set_api_key, voices, Voice, VoiceSettings, generate
import os

# Function to set up the ElevenLabs API key
set_api_key('657c3e117edd677b4f88b330b7974a1a')

def generate_audio(text, voice, output_path):
    try:
        # Generate the audio from the text using the specified voice
        audio = generate(
            text=text,
            voice=voice,
            model='eleven_monolingual_v1'  # or 'eleven_multilingual_v1' based on the voice
        )
        
        # Save the audio to the specified file path
        with open(output_path, 'wb') as f:
            f.write(audio)
        print(f"Audio saved to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")



############## Example usage

# get current directory (for file path for output)
current_directory = os.getcwd()
output_directory = os.path.join(current_directory, 'output', 'audio')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    

# select a voice for 11labs
voices = voices()
voice=voices[0]


# call the function that generates audio 
generate_audio("avatar generated based on the vibe / genra of the movie.", voice, os.path.join(output_directory, "audio1.mp3")) 
generate_audio("good reads api, in case of a new book", voice, os.path.join(output_directory, "audio2.mp3"))
generate_audio("The sun slowly sinks beneath the horizon, casting a warm glow.", voice, os.path.join(output_directory, "audio3.mp3"))
generate_audio("Sarah's heart races as she gathers her courage.", voice, os.path.join(output_directory, "audio4.mp3"))
generate_audio("She takes a deep breath and looks into their eyes.", voice, os.path.join(output_directory, "audio5.mp3"))
generate_audio("With a quivering voice, she makes her heartfelt proposal.", voice, os.path.join(output_directory, "audio6.mp3"))
generate_audio("In that fleeting moment, their love story ignites under the twinkling stars.", voice, os.path.join(output_directory, "audio7.mp3"))
