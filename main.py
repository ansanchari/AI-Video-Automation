import asyncio
import os

# Notice we are only importing the correct function names now!
from brain import generate_viral_topic, generate_video_script
from voice import generate_audio
from vision import generate_image
from motion import animate_image
from editor import edit_final_video

def main():
    print("--- Starting Fully Automated Video Pipeline ---")
    
    # 0. AUTONOMOUS IDEA GENERATION
    print("\n🧠 0. Brainstorming a brand new video topic...")
    try:
        topic = generate_viral_topic()
    except Exception as e:
        print(f"   ⚠️ Topic generator failed: {e}")
        print("   ⚠️ Falling back to default topic...")
        topic = "How a Venus Flytrap catches an insect"
        
    print(f"🤖 Final Topic: {topic}\n")
    
    # 1. The Brain (Scriptwriter)
    print("🧠 1. Generating script and scene descriptions...")
    try:
        script_data = generate_video_script(topic)
        print(f"   ✅ Script generated! Title: '{script_data['title']}'")
    except Exception as e:
        print(f"   ❌ Failed to generate script: {e}")
        return
    
    # 2. The Voice
    print("\n🎙️ 2. Generating AI voiceover...")
    audio_file = "final_audio.mp3"
    try:
        asyncio.run(generate_audio(script_data["spoken_script"], audio_file))
        print("   ✅ Voiceover saved.")
    except Exception as e:
        print(f"   ❌ Failed to generate audio: {e}")
        return
    
    # 3 & 4. The Vision & Motion
    print("\n🎨 3 & 4. Generating 3D Visuals and Animation...")
    video_clips = []
    
    for i, scene in enumerate(script_data["scenes"]):
        print(f"   -> Processing Scene {i+1} of {len(script_data['scenes'])}...")
        image_name = f"scene_{i}.jpg"
        video_name = f"scene_{i}.mp4"
        
        # Create the image
        generate_image(scene, image_name)
        
        # Animate the image
        if os.path.exists(image_name):
            animate_image(image_name, video_name)
        
        # Ensure the video actually generated before passing it to the editor
        if os.path.exists(video_name):
            video_clips.append(video_name)
            print(f"   ✅ Scene {i+1} animation complete.")
        else:
            print(f"   ⚠️ Warning: Scene {i+1} video failed. Skipping clip.")

    # 5. The Editor
    print("\n🎬 5. Stitching final video...")
    if not video_clips:
        print("   ❌ Error: No video clips successfully generated. Aborting edit.")
        return
        
    final_output_name = "zackd_style_short.mp4"
    edit_final_video(video_clips, audio_file, final_output_name)
    
    print(f"\n🎉 PIPELINE COMPLETE! Open {final_output_name} to see your result.")

if __name__ == "__main__":
    main()
