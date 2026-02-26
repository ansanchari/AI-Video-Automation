from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
import moviepy.video.fx.all as vfx

def edit_final_video(video_files, audio_file, output_filename="zackd_test.mp4"):
    print("⚙️ Starting diagnostics editor...")
    
    #1.Load Audio and force check duration
    audio = AudioFileClip(audio_file)
    print(f"🔎 DEBUG: Audio duration read as: {audio.duration} seconds")
    
    if not audio.duration or audio.duration <= 0:
        print("❌ FATAL: Audio duration is 0! Moviepy failed to read the MP3.")
        return
        
    clip_duration = audio.duration / len(video_files)
    print(f"🔎 DEBUG: Each clip will be exactly {clip_duration} seconds long")
    
    processed_clips = []
    
    #2.Process Videos with STRICT integer sizing
    for vid_path in video_files:
        clip = VideoFileClip(vid_path)
        
        #Loop to match audio
        clip = clip.fx(vfx.loop, duration=clip_duration)
        
        #Resize height to 1920 first
        clip = clip.resize(height=1920)
        
        #STRICT INTEGER MATH: Ensure width is perfectly even so x264 doesn't panic
        center_x = int(clip.w / 2)
        clip = clip.crop(x_center=center_x, width=1080, y_center=1920/2, height=1920)
        
        processed_clips.append(clip)
        print(f"✅ Processed {vid_path} - Final Size: {clip.size}")

    #3.Use 'compose' method to handle different framerates safely
    final_video = concatenate_videoclips(processed_clips, method="compose")
    final_video = final_video.set_audio(audio)
    
    print(f"⏳ Rendering final video ({final_video.duration}s)...")
    final_video.write_videofile(
        output_filename, 
        fps=24, 
        codec="libx264", 
        audio_codec="aac"
    )
    
    #4.Clean up memory
    audio.close()
    final_video.close()
    for clip in processed_clips:
        clip.close()
        
    print(f"🎬 Done. Did {output_filename} survive?")