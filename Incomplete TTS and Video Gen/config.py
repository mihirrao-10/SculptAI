"""
Configuration file for the AI Avatar Generator
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys - Load from environment variables or use defaults
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "xxxxxxxx")
TAVUS_API_KEY = os.getenv("TAVUS_API_KEY", "xxxxxxxx")  # Replace with your Tavus key

# Tavus API Configuration
TAVUS_BASE_URL = "https://tavusapi.com/v2"

# Avatar Configuration for Super Jacked Gymbro
GYMBRO_AVATAR_CONFIG = {
    "name": "GymBro_Avatar",
    "description": "Super jacked fitness enthusiast with high energy and motivation",
    "voice_settings": {
        "voice": "ash",
        "model": "gpt-4o-mini-tts",
        "instructions": "The speaker has a loud, high-energy male voice with a deep rumble, medium pace, and American-East Coast accent, like a hyped-up social media fitness enthusiast. The voice is confident and projects well."
    },
    "video_settings": {
        "quality": "high",
        "resolution": "1080p",
        "fps": 30
    }
}

# Default Scripts
DEFAULT_SCRIPTS = {
    "motivation": """
    Yo! What's up bra! You wanna get big? Bench every goddamn day! 
    Lock the fuck in dude, don't you want some huzz? 
    Time to hit the gym and get absolutely shredded! 
    No excuses, just results! Let's gooo!
    """,
    
    "workout_tips": """
    Listen up! You want gains? You gotta eat big to get big! 
    Protein, protein, protein! Hit those compound movements! 
    Squat, deadlift, bench press! That's the holy trinity! 
    No pain, no gain! Let's get it!
    """,
    
    "supplements": """
    Supplements are the cherry on top, not the main course! 
    Get your nutrition dialed in first! 
    Whey protein, creatine, maybe some pre-workout! 
    But remember, consistency beats everything!
    """
}

# Output Configuration
OUTPUT_DIR = "output"
AUDIO_FORMAT = "mp3"
VIDEO_FORMAT = "mp4"

# Video Generation Settings
MAX_GENERATION_ATTEMPTS = 30  # 5 minutes max wait time
CHECK_INTERVAL = 10  # seconds between status checks
