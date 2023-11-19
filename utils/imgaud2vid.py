import moviepy.editor as mp

def create_video_with_audio(image_path, audio_path, output_path):
    # Load the image and audio files
    image_clip = mp.ImageClip(image_path)
    audio_clip = mp.AudioFileClip(audio_path)

    # Set the duration of the video to match the audio duration
    image_clip = image_clip.set_duration(audio_clip.duration)

    # Combine the image and audio
    video_clip = image_clip.set_audio(audio_clip)

    # Specify the frames per second (fps) for the output video (e.g., 30 fps)
    video_clip.fps = 30

    # Write the final video to the output path
    video_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Example usage:
if __name__ == "__main__":

    #choosing paths
    image_path = "/home/mahdi/hackatum23/resources/image3.png"  # Replace with the actual image file path
    audio_path = "/home/mahdi/hackatum23/resources/audio3.mp3"  # Replace with the actual audio file path
    output_path = "/home/mahdi/hackatum23/output/video3.mp4"  # Replace with the desired output video file path

    #function call
    create_video_with_audio(image_path, audio_path, output_path)
