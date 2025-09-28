# AI Gymbro Avatar Generator 🏋️‍♂️

A powerful AI system that creates super jacked gymbro avatars with text-to-speech and lip-sync capabilities using OpenAI and Tavus APIs.

## Features

- 🎤 **High-Quality Text-to-Speech**: Uses OpenAI's GPT-4o-mini TTS with custom voice settings
- 🎬 **AI Avatar Generation**: Creates realistic avatars using Tavus API
- 👄 **Perfect Lip-Sync**: Synchronizes avatar mouth movements with audio
- 💪 **Gymbro Personality**: Configured for high-energy fitness content
- 🎯 **Customizable Scripts**: Easy to modify for different content types

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Edit `config.py` and add your API keys:

```python
OPENAI_API_KEY = "your_actual_openai_api_key"
TAVUS_API_KEY = "your_actual_tavus_api_key"
```

### 3. Prepare Source Video (Optional but Recommended)

For the best results, provide a 2-minute video of a super jacked person:
- Upload the video file to your project directory
- Update the `source_video_path` in your scripts

## Usage

### Basic Usage

```python
from avatar_generator import AvatarGenerator
from config import OPENAI_API_KEY, TAVUS_API_KEY

# Initialize generator
generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)

# Create avatar with custom script
script = "Yo! What's up bra! You wanna get big? Bench every goddamn day!"
result = generator.create_gymbro_avatar(script)

if result:
    print(f"Avatar created: {result}")
```

### Using Pre-built Examples

```bash
python example_usage.py
```

This will create:
- Motivational gymbro video
- Workout tips video  
- Custom script video

### Custom Scripts

```python
custom_script = """
Bro, you think you're tough? You think you're strong? 
Well, the gym doesn't care about your excuses! 
Every rep counts, every set matters! 
You want to be a champion? Act like one! 
Let's go get this bread! 💪
"""

result = generator.create_gymbro_avatar(custom_script)
```

## File Structure

```
├── avatar_generator.py    # Main avatar generation class
├── config.py             # Configuration and settings
├── example_usage.py      # Example usage scripts
├── requirements.txt      # Python dependencies
├── texttospeech.py      # Original TTS script
└── output/              # Generated videos and audio files
```

## API Requirements

### OpenAI API
- **Model**: GPT-4o-mini TTS
- **Voice**: "ash" (high-energy male voice)
- **Usage**: Text-to-speech generation

### Tavus API
- **Purpose**: Avatar creation and lip-sync
- **Requirements**: 2-minute source video for best results
- **Features**: Real-time lip-sync, voice cloning

## Configuration Options

### Voice Settings
```python
voice_settings = {
    "voice": "ash",
    "model": "gpt-4o-mini-tts",
    "instructions": "High-energy male voice with deep rumble..."
}
```

### Avatar Settings
```python
avatar_config = {
    "name": "GymBro_Avatar",
    "description": "Super jacked fitness enthusiast",
    "quality": "high",
    "resolution": "1080p"
}
```

## Output

The system generates:
- **Audio files**: High-quality MP3 files with gymbro voice
- **Video files**: MP4 files with lip-synced avatar
- **Logs**: Detailed logging for debugging

## Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure both OpenAI and Tavus API keys are correctly set
2. **Video Generation Timeout**: Increase `MAX_GENERATION_ATTEMPTS` in config
3. **Audio Quality**: Check OpenAI API quota and model availability
4. **Lip-Sync Issues**: Ensure source video is high quality and well-lit

### Debug Mode

Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Advanced Usage

### Custom Avatar Sources

```python
# Provide your own jacked gymbro video
source_video_path = "path/to/your/gymbro_video.mp4"
result = generator.create_gymbro_avatar(script, source_video_path)
```

### Batch Processing

```python
scripts = [
    "Motivational speech 1...",
    "Workout tips...",
    "Supplement advice..."
]

for i, script in enumerate(scripts):
    result = generator.create_gymbro_avatar(script)
    print(f"Video {i+1} created: {result}")
```

## License

This project is for educational and personal use. Please ensure you comply with OpenAI and Tavus API terms of service.

## Support

For issues or questions:
1. Check the logs in the console output
2. Verify API keys and quotas
3. Ensure source video meets Tavus requirements
4. Check network connectivity for API calls
