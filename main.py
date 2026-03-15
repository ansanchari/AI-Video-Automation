import asyncio
import os
import shutil
from brain import generate_viral_topic, generate_video_script
from voice import generate_audio
from vision import generate_image
from motion import animate_image
from editor import edit_final_video

TEMP_DIR="temp_scratch"
EXPORT_DIR="final_exports"

def setup_directories():
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(EXPORT_DIR, exist_ok=True)

def main():
    print("Starting Fully Automated Video Pipeline")
    
    setup_directories()
    
    topic=generate_viral_topic()
    
    script_data=generate_video_script(topic)
    
    audio_file=os.path.join(TEMP_DIR, "final_audio.mp3")
    asyncio.run(generate_audio(script_data["spoken_script"], audio_file))
    
    video_clips=[]
    for i, scene in enumerate(script_data["scenes"]):
        image_name=os.path.join(TEMP_DIR, f"scene_{i}.jpg")
        video_name=os.path.join(TEMP_DIR, f"scene_{i}.mp4")
        
        generate_image(scene, image_name)
        if os.path.exists(image_name):
            animate_image(image_name, video_name)
            video_clips.append(video_name)

    final_output_name=os.path.join(EXPORT_DIR, "zackd_style_short.mp4")
    edit_final_video(video_clips, audio_file, final_output_name)
    
    print(f"\FULL PIPELINE COMPLETE! Video safely exported to: {final_output_name}")
    

    print("\n Executing safe cleanup of intermediate files...")
    shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True) # Recreate empty scratch folder for the next run
    print("Cleanup complete.")

if __name__ == "__main__":
    main()
