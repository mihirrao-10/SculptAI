# 🏋️‍♂️ AI Gymbro Avatar Generator - Setup Guide

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Keys

#### Option A: Using Environment Variables (Recommended)

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit `.env` file and add your API keys:
```bash
OPENAI_API_KEY=sk-your-actual-openai-key-here
TAVUS_API_KEY=your-actual-tavus-key-here
```

#### Option B: Direct Configuration

Edit `config.py` and replace the placeholder values:
```python
OPENAI_API_KEY = "sk-your-actual-openai-key-here"
TAVUS_API_KEY = "your-actual-tavus-key-here"
```

### 3. Get Your API Keys

#### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up/Login to your account
3. Click "Create new secret key"
4. Copy the key (starts with `sk-`)

#### Tavus API Key
1. Go to [Tavus.io](https://tavus.io)
2. Sign up for an account
3. Get your API key from the dashboard

### 4. Run the Project

#### Basic Text-to-Speech Only
```bash
python texttospeech.py
```
This will generate `speech.mp3` in the project directory.

#### Full Avatar Generation
```bash
python example_usage.py
```

#### Custom Script
```python
from avatar_generator import AvatarGenerator
from config import OPENAI_API_KEY, TAVUS_API_KEY

generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)
script = "Your custom gymbro script here!"
result = generator.create_gymbro_avatar(script)
```

## File Structure

```
ai_gymbro_avatar/
├── avatar_generator.py    # Main avatar generation class
├── texttospeech.py        # Standalone TTS script
├── config.py              # Configuration and API keys
├── example_usage.py       # Example usage scripts
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .env                   # Your actual API keys (create this)
├── output/                # Generated videos and audio files
└── speech.mp3             # Generated TTS audio (after running)
```

## Usage Examples

### 1. Simple Text-to-Speech
```python
# Edit texttospeech.py and change the API key
python texttospeech.py
```

### 2. Generate Avatar with Custom Script
```python
from avatar_generator import AvatarGenerator
from config import OPENAI_API_KEY, TAVUS_API_KEY

generator = AvatarGenerator(OPENAI_API_KEY, TAVUS_API_KEY)

custom_script = """
Bro, you think you're tough? You think you're strong? 
Well, the gym doesn't care about your excuses! 
Every rep counts, every set matters! 
You want to be a champion? Act like one! 
Let's go get this bread! 💪
"""

result = generator.create_gymbro_avatar(custom_script)
```

### 3. Use Pre-built Examples
```python
python example_usage.py
```

## Troubleshooting

### Common Issues

1. **"API key not found" error**
   - Make sure you've set your API keys in `.env` or `config.py`
   - Check that your OpenAI API key starts with `sk-`

2. **"Module not found" errors**
   - Run `pip install -r requirements.txt`
   - Make sure you're in the correct directory

3. **Audio generation fails**
   - Check your OpenAI API quota
   - Verify your API key is valid
   - Try a shorter script first

4. **Video generation fails**
   - Tavus API requires a source video for best results
   - Check your Tavus API key and quota
   - Ensure you have a 2-minute video of a person for avatar creation

### Debug Mode

Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Output Files

- `speech.mp3` - Generated audio file
- `output/` directory - Contains all generated videos and audio files
- Console logs - Detailed information about the generation process

## API Costs

- **OpenAI TTS**: ~$0.015 per 1K characters
- **Tavus Video**: Varies by plan and video length
- **Estimated cost**: $0.50-2.00 per video depending on length

## Next Steps

1. Try the basic TTS first: `python texttospeech.py`
2. Test with a custom script
3. Add your own source video for better avatar results
4. Experiment with different voice settings in `config.py`

## Support

If you encounter issues:
1. Check the console output for error messages
2. Verify your API keys are correct
3. Ensure you have sufficient API quota
4. Try with shorter scripts first
