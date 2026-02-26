import asyncio
import edge_tts

async def generate_audio(text, output_filename="voiceover.mp3"):
    communicate = edge_tts.Communicate(text, "en-US-ChristopherNeural")
    await communicate.save(output_filename)
    print(f"Audio saved as {output_filename}")
