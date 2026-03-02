from moviepy.editor import VideoFileClip, concatenate_videoclips

print(" Running Bare Minimum Diagnostic ")

clip1 = VideoFileClip("scene_0.mp4")
clip2 = VideoFileClip("scene_1.mp4")

final_video = concatenate_videoclips([clip1, clip2])

print(f" Rendering bare minimum video. Duration: {final_video.duration} seconds...")
final_video.write_videofile(
    "diagnostic.mp4", 
    fps=24, 
    codec="libx264"
)

clip1.close()
clip2.close()
final_video.close()

print("Diagnostic complete. Check your folder for diagnostic.mp4")
