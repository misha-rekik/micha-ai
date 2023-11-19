# Import everything needed to edit video clips
from moviepy.editor import *
 
# loading video dsa gfg intro video
clip = VideoFileClip("/home/mahdi/hackatum23/output/video1.mp4")
 
# getting subclip as video is large
#clip1 = clip.subclip(0, 5)
 
 
# loading video gfg
clipx = VideoFileClip("/home/mahdi/hackatum23/output/video2.mp4")
 
# getting subclip 
#clip2 = clipx.subclip(0, 5)
 
# clip list
clips = [clip, clipx]
 
# concatenating both the clips
final = concatenate_videoclips(clips)
 
# showing final clip
final.ipython_display(width = 480)