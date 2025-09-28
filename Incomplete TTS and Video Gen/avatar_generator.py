import os
import time
import requests
import json
from pathlib import Path
from openai import OpenAI
from typing import Optional, Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AvatarGenerator:
    """
    AI Avatar Generator that combines OpenAI TTS with Tavus video generation
    Creates a super jacked gymbro avatar with lip-sync capabilities
    """
    
    def __init__(self, openai_api_key: str, tavus_api_key: str):
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.tavus_api_key = tavus_api_key
        self.tavus_base_url = "https://tavusapi.com/v2"
        self.output_dir = Path(__file__).parent / "output"
        self.output_dir.mkdir(exist_ok=True)
        
        # Gymbro avatar configuration
        self.avatar_config = {
            "name": "GymBro_Avatar",
            "description": "Super jacked fitness enthusiast with high energy",
            "voice_settings": {
                "voice": "ash",
                "model": "gpt-4o-mini-tts",
                "instructions": "The speaker has a loud, high-energy male voice with a deep rumble, medium pace, and American-East Coast accent, like a hyped-up social media fitness enthusiast. The voice is confident and projects well."
            }
        }
    
    def generate_audio(self, text: str, output_filename: str = "speech.mp3") -> Path:
        """
        Generate TTS audio using OpenAI API
        """
        logger.info(f"Generating audio for text: {text[:50]}...")
        
        speech_file_path = self.output_dir / output_filename
        
        try:
            with self.openai_client.audio.speech.with_streaming_response.create(
                model=self.avatar_config["voice_settings"]["model"],
                voice=self.avatar_config["voice_settings"]["voice"],
                input=text,
                instructions=self.avatar_config["voice_settings"]["instructions"],
            ) as response:
                response.stream_to_file(speech_file_path)
            
            logger.info(f"Audio generated successfully: {speech_file_path}")
            return speech_file_path
            
        except Exception as e:
            logger.error(f"Error generating audio: {e}")
            raise
    
    def create_avatar_source(self, video_file_path: str) -> Optional[str]:
        """
        Create an avatar source in Tavus using a video file
        This would typically be a 2-minute video of a jacked gymbro
        """
        logger.info("Creating avatar source in Tavus...")
        
        headers = {
            "x-api-key": self.tavus_api_key,
            "Content-Type": "application/json"
        }
        
        # Upload video file to Tavus
        with open(video_file_path, 'rb') as video_file:
            files = {'video': video_file}
            data = {
                'name': self.avatar_config["name"],
                'description': self.avatar_config["description"]
            }
            
            try:
                response = requests.post(
                    f"{self.tavus_base_url}/v1/sources",
                    headers=headers,
                    files=files,
                    data=data
                )
                
                if response.status_code == 201:
                    source_data = response.json()
                    source_id = source_data.get('id')
                    logger.info(f"Avatar source created with ID: {source_id}")
                    return source_id
                else:
                    logger.error(f"Failed to create avatar source: {response.text}")
                    return None
                    
            except Exception as e:
                logger.error(f"Error creating avatar source: {e}")
                return None
    
    def generate_video_with_lipsync(self, source_id: str, audio_file_path: Path, script: str) -> Optional[str]:
        """
        Generate video with lip-sync using Tavus API
        """
        logger.info("Generating video with lip-sync...")
        
        headers = {
            "x-api-key": self.tavus_api_key,
            "Content-Type": "application/json"
        }
        
        # Upload audio file
        with open(audio_file_path, 'rb') as audio_file:
            files = {'audio': audio_file}
            data = {
                'source_id': source_id,
                'script': script,
                'voice_settings': self.avatar_config["voice_settings"]
            }
            
            try:
                response = requests.post(
                    f"{self.tavus_base_url}/v1/videos",
                    headers=headers,
                    files=files,
                    data=data
                )
                
                if response.status_code == 201:
                    video_data = response.json()
                    video_id = video_data.get('id')
                    logger.info(f"Video generation started with ID: {video_id}")
                    return video_id
                else:
                    logger.error(f"Failed to start video generation: {response.text}")
                    return None
                    
            except Exception as e:
                logger.error(f"Error generating video: {e}")
                return None
    
    def check_video_status(self, video_id: str) -> Dict[str, Any]:
        """
        Check the status of video generation
        """
        headers = {
            "x-api-key": self.tavus_api_key
        }
        
        try:
            response = requests.get(
                f"{self.tavus_base_url}/v1/videos/{video_id}",
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                logger.error(f"Failed to check video status: {response.text}")
                return {}
                
        except Exception as e:
            logger.error(f"Error checking video status: {e}")
            return {}
    
    def download_video(self, video_url: str, output_filename: str = "gymbro_avatar.mp4") -> Path:
        """
        Download the generated video
        """
        logger.info(f"Downloading video from: {video_url}")
        
        try:
            response = requests.get(video_url)
            response.raise_for_status()
            
            video_path = self.output_dir / output_filename
            with open(video_path, 'wb') as f:
                f.write(response.content)
            
            logger.info(f"Video downloaded successfully: {video_path}")
            return video_path
            
        except Exception as e:
            logger.error(f"Error downloading video: {e}")
            raise
    
    def create_gymbro_avatar(self, script: str, source_video_path: Optional[str] = None) -> Optional[Path]:
        """
        Main method to create a gymbro avatar with the given script
        """
        logger.info("Starting gymbro avatar creation process...")
        
        try:
            # Step 1: Generate audio
            audio_path = self.generate_audio(script)
            
            # Step 2: Create avatar source (if source video provided)
            source_id = None
            if source_video_path and os.path.exists(source_video_path):
                source_id = self.create_avatar_source(source_video_path)
                if not source_id:
                    logger.warning("Failed to create avatar source, proceeding without custom avatar")
            else:
                logger.warning("No source video provided, using default avatar")
            
            # Step 3: Generate video with lip-sync
            if source_id:
                video_id = self.generate_video_with_lipsync(source_id, audio_path, script)
                
                if video_id:
                    # Step 4: Wait for video generation to complete
                    logger.info("Waiting for video generation to complete...")
                    max_attempts = 30  # 5 minutes max
                    attempt = 0
                    
                    while attempt < max_attempts:
                        status = self.check_video_status(video_id)
                        
                        if status.get('status') == 'completed':
                            video_url = status.get('video_url')
                            if video_url:
                                return self.download_video(video_url)
                            else:
                                logger.error("Video completed but no URL provided")
                                return None
                        elif status.get('status') == 'failed':
                            logger.error(f"Video generation failed: {status.get('error', 'Unknown error')}")
                            return None
                        
                        time.sleep(10)  # Wait 10 seconds before checking again
                        attempt += 1
                    
                    logger.error("Video generation timed out")
                    return None
                else:
                    logger.error("Failed to start video generation")
                    return None
            else:
                logger.warning("No avatar source available, returning audio only")
                return audio_path
                
        except Exception as e:
            logger.error(f"Error in avatar creation process: {e}")
            return None

def main():
    """
    Example usage of the AvatarGenerator
    """
    # Configuration - Replace with your actual API keys
    OPENAI_API_KEY = "your_openai_api_key_here"
    TAVUS_API_KEY = "your_tavus_api_key_here"
    
    # Initialize the generator
    generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)
    
    # Gymbro script
    script = """
    Yo! What's up bra! You wanna get big? Bench every goddamn day! 
    Lock the fuck in dude, don't you want some huzz? 
    Time to hit the gym and get absolutely shredded! 
    No excuses, just results! Let's gooo!
    """
    
    # Optional: Path to source video of a jacked gymbro (2 minutes recommended)
    source_video_path = None  # "path/to/your/gymbro_video.mp4"
    
    # Create the avatar
    result_path = generator.create_gymbro_avatar(script, source_video_path)
    
    if result_path:
        print(f"Avatar created successfully: {result_path}")
    else:
        print("Failed to create avatar")

if __name__ == "__main__":
    main()
