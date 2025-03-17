## Directory Structure
|– task1_Yardstick_working_pipeline/                   
|– task_2_web_scraper/                 
|– Demo_Yardstick.mov         
|– requirements.txt       



## Directory Structure
```plaintext
├── config/
│   └── Contains configuration files, including:
│       - YouTube video URL.
|       - Output Path for AI generated voice
│       - ElevenLabs API keys .
│
├── downloads/
│   └── Stores downloaded files, including YouTube video audio.
│
├── logs/
│   └── Contains log files to track the execution of the pipeline and debug issues.
│
├── pipelien/
│   └── Combines various stages of the process into a single pipeline function.
│
├── src/
│   └── Includes core functionality for:
│       - Logging setup.
│       - Constants for program behavior.
│
├── stages/
│   └── Contains individual stages of the pipeline for:
│       - YouTube audio extraction.
│       - Text generation.
│       - AI audio generation.
│
├── test/
│   └── Includes test cases to ensure the functionality works as expected.
│
├── utils/
│   └── Utility scripts for tasks such as:
│       - Reading YAML files.
│       - Handling reusable operations.
│
├── .env
│   └── Environment file to store sensitive keys such as ElevenLabs API keys.
│
├── main.py
│   └── Entry point for running the program. Combines the pipeline for end-to-end execution.


# YardStick - Audio Content Pipeline

## Overview
YardStick is a Python-based pipeline that automates the process of:
1. Downloading audio from YouTube videos
2. Converting speech to text using Deepgram API
3. Generating new audio content using ElevenLabs AI voice synthesis

## Features
- YouTube audio extraction
- Speech-to-text transcription
- AI-powered voice synthesis
- Configurable pipeline stages
- Logging system for tracking execution
- Web scraping capabilities (task_2_web_scraper)

## Technology Stack
- **Python 3.11+**
- **APIs Used:**
  - Deepgram API (Speech-to-text)
  - ElevenLabs API (Text-to-speech)
  - YouTube-DLP (Video downloading)
- **Key Libraries:**
  - `yt-dlp`: YouTube video/audio downloading
  - `deepgram-sdk`: Speech recognition
  - `requests`: HTTP requests
  - `python-dotenv`: Environment management
  - `PyYAML`: Configuration management
  - `beautifulsoup4`: Web scraping (task_2)

## Setup and Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager
- FFmpeg (for audio processing)

### Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/YardStick.git
cd YardStick
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create `.env` file in the root directory with your API keys:
```
deepgram_api_key="your_deepgram_api_key"
eleven_labs_api_key="your_eleven_labs_api_key"
```

### Configuration
1. Update `config/config.yaml` with your settings:
```yaml
yt_video_download:
  url: "your_youtube_url"
  output_path: "downloads"

eleven_labs:
  voice_id: "your_voice_id"
```

## Usage

### Running the Pipeline
Execute the main script to run the complete pipeline:
```bash
python main.py
```

The pipeline will:
1. Download audio from the configured YouTube URL
2. Transcribe the audio to text
3. Generate new audio using ElevenLabs

## Error Handling
- The pipeline includes comprehensive logging
- Logs are stored in `logs/running_logs.log`
- Each stage includes error handling and status reporting

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Acknowledgments
- Deepgram for speech-to-text API
- ElevenLabs for voice synthesis
- YouTube-DLP contributors
