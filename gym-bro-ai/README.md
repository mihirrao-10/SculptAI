# Sculpt - AI Training Partner

A ChatGPT interface with image upload capabilities and David Goggins voice text-to-speech powered by OpenAI and ElevenLabs.

## Features

- 💬 Chat with AI using OpenAI's GPT-4 Vision
- 📸 Upload images for AI analysis
- 🎤 David Goggins voice text-to-speech
- 🎨 Modern, motivational UI design
- 📱 Responsive design

## Setup

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Set up environment variables:**
   Copy `env.example` to `.env.local` and fill in your API keys:
   ```bash
   cp env.example .env.local
   ```

   Required API keys:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `ELEVENLABS_API_KEY`: Your ElevenLabs API key
   - `ELEVENLABS_VOICE_ID`: David Goggins voice ID from ElevenLabs

3. **Run the development server:**
   ```bash
   npm run dev
   ```

4. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## API Keys Setup

### OpenAI API Key
1. Go to [OpenAI Platform](https://platform.openai.com/)
2. Create an account and get your API key
3. Add it to your `.env.local` file

### ElevenLabs API Key & Voice ID
1. Go to [ElevenLabs](https://elevenlabs.io/)
2. Create an account and get your API key
3. Find a David Goggins voice clone or similar motivational voice
4. Get the voice ID from the voice settings
5. Add both to your `.env.local` file

## Usage

1. **Text Chat**: Type your message and press Enter
2. **Image Upload**: Click the image icon to upload an image
3. **Voice Recording**: Click the microphone icon (coming soon)
4. **Audio Playback**: Click the speaker icon to replay the AI's response

## Tech Stack

- **Frontend**: Next.js 14, React, TypeScript, Tailwind CSS
- **Backend**: Next.js API Routes
- **AI**: OpenAI GPT-4 Vision
- **TTS**: ElevenLabs API
- **UI**: Lucide React icons, Framer Motion

## Project Structure

```
sculpt/
├── app/
│   ├── api/
│   │   ├── chat/route.ts      # OpenAI integration
│   │   └── tts/route.ts       # ElevenLabs TTS
│   ├── globals.css            # Global styles
│   ├── layout.tsx             # App layout
│   └── page.tsx               # Main chat interface
├── components/                # Reusable components (future)
├── env.example               # Environment variables template
├── package.json              # Dependencies
├── tailwind.config.js        # Tailwind configuration
└── tsconfig.json             # TypeScript configuration
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

MIT License - see LICENSE file for details
