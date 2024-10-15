import requests
import os
from utils.utils_1 import read_from_file
from utils.utils_1 import read_yaml
from src.constatns import *
eleven_config = read_yaml(CONFIG_FILEPATH)
voice_id = eleven_config.eleven_labs.voice_id
class cvt_text_to_audio:
    def __init__(
            self,
            filename,
            api_key=os.environ["eleven_labs_api_key"], 
            voice_id=voice_id
            ) :
        self.filetext =read_from_file(filename)
        self.api_key = api_key
        self.voice_id = voice_id

    def Covnert_text_to_audio(self):
        """
        Convert text file to audio
        """
        if not self.filetext.strip():
            print("No text to convert to audio.")
            return
        url = f'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}'
        headers = {
            'xi-api-key': self.api_key,
            'Content-Type': 'application/json'
        }
        data = {
            'text': self.filetext,
            'voice_settings': {'stability': 0.75, 'similarity_boost': 0.75}
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            with open('output_audio.mp3', 'wb') as f:
                f.write(response.content)
            print(f"Generated audio saved to 'output_audio.mp3'")
        else:
            print(f"Error: {response.status_code} - {response.text}")



        