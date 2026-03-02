import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

client=genai.Client()

def generate_viral_topic():
    print(" 0. Brainstorming a brand new video topic...")
    
    brainstorm_prompt = """
    You are a viral YouTube Shorts producer for Zack D. Films. 
    Give me exactly ONE fascinating, highly visual educational topic about science, human anatomy, or nature that would make a great 3D animated video. 
    It must be under 8 words. 
    Output ONLY the topic string, with no quotes, no formatting, and no extra text.
    Example output: How a chameleon changes its skin color
    """
    
    try:
        response=client.models.generate_content(
            model='gemini-2.5-flash',
            contents=brainstorm_prompt,
        )
        topic=response.text.strip()
        print(f"       Eureka! The AI chose: '{topic}'")
        return topic
    except Exception as e:
        print(f"       Brainstorming failed: {e}")
        
        return "How the human eye focuses on light"

def generate_video_script(topic):
    prompt = f"""
    You are a technical director for a 3D educational animation studio like Zack D. Films.
    Write a 30-second script about: {topic}.

    Output ONLY a valid JSON object with this exact structure:
    {{
      "title": "Video Title",
      "spoken_script": "The exact words the voiceover will say.",
      "scenes": [
        "Scene 1 technical visual description",
        "Scene 2 technical visual description",
        "Scene 3 technical visual description",
        "Scene 4 technical visual description"
      ]
    }}
    
    CRITICAL INSTRUCTION FOR SCENES: 
    Do NOT write artistic or narrative descriptions. Write instructions for a 3D modeler.
    Use clinical, anatomical, and technical terms. 
    Describe the exact camera angle (e.g., "Extreme close-up cross-section").
    Specify a clean, neutral background so the subject is clear.
    Example Bad Scene: "The fly lands happily on the leaf."
    Example Good Scene: "Extreme close-up 3D render, cross-section view of venus flytrap leaf mechanism, small housefly triggering sensitive hairs, plain grey studio background, educational diagram style."
    """
    
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        
        clean_json = response.text.replace('```json', '').replace('```', '').strip()
        return json.loads(clean_json)
    except Exception as e:
        print(f" Error generating script: {e}")
        raise e
