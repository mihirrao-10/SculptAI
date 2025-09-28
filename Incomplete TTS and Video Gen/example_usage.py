"""
Example usage of the AI Avatar Generator
This script demonstrates how to create a super jacked gymbro avatar
"""

from avatar_generator import AvatarGenerator
from config import OPENAI_API_KEY, TAVUS_API_KEY, DEFAULT_SCRIPTS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_motivational_video():
    """
    Create a motivational gymbro video
    """
    print("🏋️‍♂️ Creating motivational gymbro avatar...")
    
    # Initialize the generator
    generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)
    
    # Use the motivation script
    script = DEFAULT_SCRIPTS["motivation"]
    
    # Optional: Path to source video of a jacked gymbro (2 minutes recommended)
    # You would need to provide a video file of a super jacked person for best results
    source_video_path = None  # "path/to/your/gymbro_video.mp4"
    
    # Create the avatar
    result_path = generator.create_gymbro_avatar(script, source_video_path)
    
    if result_path:
        print(f"✅ Avatar created successfully: {result_path}")
        return result_path
    else:
        print("❌ Failed to create avatar")
        return None

def create_workout_tips_video():
    """
    Create a workout tips video
    """
    print("💪 Creating workout tips gymbro avatar...")
    
    generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)
    script = DEFAULT_SCRIPTS["workout_tips"]
    
    result_path = generator.create_gymbro_avatar(script)
    
    if result_path:
        print(f"✅ Workout tips avatar created: {result_path}")
        return result_path
    else:
        print("❌ Failed to create workout tips avatar")
        return None

def create_custom_script_video(custom_script: str):
    """
    Create a video with a custom script
    """
    print("🎯 Creating custom script gymbro avatar...")
    
    generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)
    
    result_path = generator.create_gymbro_avatar(custom_script)
    
    if result_path:
        print(f"✅ Custom avatar created: {result_path}")
        return result_path
    else:
        print("❌ Failed to create custom avatar")
        return None

def main():
    """
    Main function to demonstrate the avatar generator
    """
    print("🚀 AI Gymbro Avatar Generator")
    print("=" * 50)
    
    # Check if API keys are set
    if OPENAI_API_KEY == "your_openai_api_key_here":
        print("⚠️  Please set your OpenAI API key in config.py")
        return
    
    if TAVUS_API_KEY == "your_tavus_api_key_here":
        print("⚠️  Please set your Tavus API key in config.py")
        return
    
    # Create different types of videos
    print("\n1. Creating motivational video...")
    motivational_video = create_motivational_video()
    
    print("\n2. Creating workout tips video...")
    tips_video = create_workout_tips_video()
    
    print("\n3. Creating custom script video...")
    custom_script = """
    Bro, you think you're tough? You think you're strong? 
    Well, the gym doesn't care about your excuses! 
    Every rep counts, every set matters! 
    You want to be a champion? Act like one! 
    Let's go get this bread! 💪
    """
    custom_video = create_custom_script_video(custom_script)
    
    print("\n🎉 Avatar generation complete!")
    print("Check the 'output' directory for your generated videos.")

if __name__ == "__main__":
    main()
