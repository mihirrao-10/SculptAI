from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key="xxxxxx")
speech_file_path = Path(__file__).parent / "speech.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="ash",
    input="Yo! What's up bra! You wanna get big? Bench every goddamn day! Lock the fuck in dude, don't you want some huzz?",
    instructions="The speaker has a loud, high-energy male voice with a deep rumble, medium pace, and American-East Coast accent, like a hyped-up social media fitness enthusiast. The voice is confident and projects well.",
) as response:
    response.stream_to_file(speech_file_path)