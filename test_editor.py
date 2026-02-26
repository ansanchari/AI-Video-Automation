from moviepy.editor import VideoFileClip, concatenate_videoclips

print("--- Running Bare Minimum Diagnostic ---")

#1.Load just the first two raw clips (no resizing, no looping)
clip1 = VideoFileClip("scene_0.mp4")
clip2 = VideoFileClip("scene_1.mp4")

#2.Stitch them together
final_video = concatenate_videoclips([clip1, clip2])

#3.Export WITHOUT audio
print(f"⏳ Rendering bare minimum video. Duration: {final_video.duration} seconds...")
final_video.write_videofile(
    "zackd_diagnostic.mp4", 
    fps=24, 
    codec="libx264"
)

#4.Clean up
clip1.close()
clip2.close()
final_video.close()

print("🎬 Diagnostic complete. Check your folder for zackd_diagnostic.mp4")