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


