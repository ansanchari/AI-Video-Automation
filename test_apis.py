import os
import requests
from google import genai
from dotenv import load_dotenv

load_dotenv()

gemini_key = os.getenv("GEMINI_API_KEY")
hf_token = os.getenv("HUGGINGFACE_TOKEN")

print(" Starting API Tests \n")

print("Testing Gemini API...")
if not gemini_key:
    print(" Error: GEMINI_API_KEY not found in .env file.")
else:
    try:
        client = genai.Client()
        
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents="Respond with exactly this text: Gemini is connected!"
        )
        print(f" Success! Gemini: {response.text.strip()}")
    except Exception as e:
        print(f" Gemini Error: {e}")

print("\n--------------------------\n")

print("Testing Hugging Face API...")
if not hf_token:
    print(" Error: HUGGINGFACE_TOKEN not found in .env file.")
else:
    try:
        auth_url = "https://huggingface.co/api/whoami-v2"
        headers = {"Authorization": f"Bearer {hf_token}"}
        
        response = requests.get(auth_url, headers=headers)
        
        if response.status_code == 200:
            user_data = response.json()
            print(f" Success! Connected to Hugging Face as: {user_data.get('name')}")
        elif response.status_code == 401:
            print(" Error: Unauthorized. Your Hugging Face token is invalid or expired.")
        else:
            print(f" Error: Received status code {response.status_code}. {response.text}")
    except Exception as e:
        print(f" Hugging Face Request Error: {e}")

print("\n Tests Complete ")
