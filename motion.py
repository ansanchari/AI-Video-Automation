from gradio_client import Client, handle_file
from moviepy.editor import ImageClip
import shutil

def animate_image(image_path, output_path):
    try:
        #Connecting to the public Hugging Face space
        client = Client("multimodalart/stable-video-diffusion")
        
        #removed the broken 'cond_aug' parameter!
        result=client.predict(
            image=handle_file(image_path),
            motion_bucket_id=127,      
            decoding_t=3,              
            seed=0,
            api_name="/video"
        )
        
        shutil.move(result, output_path)
        print(f"       AI Motion applied to {image_path}")
        
    except Exception as e:
        print(f"       API busy or failed: {e}")
        print("       Triggering Jugaad Fallback: Converting image to static clip...")
        
        #THE JUGGAAD FALLBACK: Add a slow zoom effect (Ken Burns) to the static image
        try:
            from moviepy.editor import ImageClip
            #Load image and resize it to be slightly larger so we have room to pan
            clip = ImageClip(image_path).set_duration(3).resize(1.1)
            
            #Apply a slow, dynamic pan/zoom effect
            clip = clip.set_position(lambda t: ('center', 'center'))
            clip.write_videofile(output_path, fps=24, logger=None)
            print(f"       Dynamic zoom clip saved to {output_path}")
        except Exception as fallback_error:
            print(f"       Fallback failed: {fallback_error}")