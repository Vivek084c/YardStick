import os
import asyncio
import yt_dlp
from deepgram import Deepgram
from dotenv import load_dotenv
load_dotenv()
from src.Log import logger

api_key = os.environ["deepgram_api_key"]


class cvt_audio_to_text:
    def __init__(
            self,
            api_key=os.environ["deepgram_api_key"],
            filename=""
            ) :
        self.api_key = api_key
        self.filename = filename
    async def Convert_to_text(self):
        """
        Returns the text for the given audio file
        Args:
            -
        Return:
            text: transcribed text
        """
        logger.info("Started the Transcribing process")
        deepgram = Deepgram(self.api_key)
        with open(f"downloads/{self.filename}.mp3", 'rb') as audio:
            source = {'buffer': audio, 'mimetype': 'audio/mp3'}
            response = await deepgram.transcription.prerecorded(source, {'punctuate': True})
            if response and 'results' in response and response['results']['channels']:
                text = response['results']['channels'][0]['alternatives'][0]['transcript']
                logger.info(f"Transcription Done ")
                return text
            else:
                logger.error("Transcription failed or no results returned.")
                return ""

