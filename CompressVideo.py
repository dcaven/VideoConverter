from moviepy.editor import * #pip install MoviePy

def cutAndCompressVideo():
    clip = VideoFileClip("C:\\Users\\David Caven\\Documents\\Python\\filename.mp4").resize(0.5)
    subclip = (clip.subclip(221,232)) #start time in seconds, end time in seconds
    print(subclip.duration)
    # subclip.write_gif("clip_output.gif") # ~300MB/10sec
    subclip.write_videofile(filename="C:\\Users\\David Caven\\Documents\\Python\\clip_output.mp4", fps=30, codec="libx264") # ~11MB/10sec
print("Starting conversion")
cutAndCompressVideo()
print("Conversion Complete")