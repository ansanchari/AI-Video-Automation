import os
import requests
from dotenv import load_dotenv

load_dotenv()
HF_TOKEN=os.getenv("HUGGINGFACE_TOKEN")

API_URL="https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

def generate_image(prompt, output_filename="scene.jpg"):
    print(f"       Generating high-end cinematic 3D image via Hugging Face...")
    headers={"Authorization": f"Bearer {HF_TOKEN}"}
    
    #keywords for high-end rendering engines and realistic lighting.
    style_prompt=f"hyper-realistic 3D render, Unreal Engine 5 cinematic, 8k textures, highly detailed, subsurface scattering, volumetric lighting, octane render, sharp focus, centered subject, {prompt}"
    
    #removed 'cinematic' and 'depth of field' from the ban list to make it less flat.
    negative_prompt="cartoon, painting, drawing, grainy, low resolution, pixelated, ugly, messy background, out of focus, blurry, oversaturated, watermark, text"
    
    #Send both prompts to the API
    payload={
        "inputs": style_prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
            #Boosting steps and guidance for maximum detail adherence
            "num_inference_steps": 35, 
            "guidance_scale": 8.0      
        }
    }
    
    try:
        response=requests.post(API_URL, headers=headers, json=payload)
        if response.status_code==200:
            with open(output_filename, 'wb') as f:
                f.write(response.content)
            print(f"       Saved {output_filename}")
            return True
        else:
            print(f"       API Error: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"       Image generation error: {e}")
        return False