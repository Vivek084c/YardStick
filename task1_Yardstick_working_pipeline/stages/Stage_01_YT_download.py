from src.constatns import *
from utils.utils_1 import read_yaml
import asyncio
import yt_dlp
import os
from src.Log import logger

class yt_download:
    def __init__(
            self,
            YT_CONFIG=read_yaml(CONFIG_FILEPATH)
            ) :
        self.url = YT_CONFIG.yt_video_download.url
        self.output_path = YT_CONFIG.yt_video_download.output_path

    def Download_YT_video(self):
        url = self.url
        output_path = self.output_path
        """
        Downloads Youtube video and save it
        Args:
            url - url of youtube video to be downloaded
            output_path - path of save directory
        Return:
            fileName - file name of the downloaded video
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(output_path, '%(id)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': False,
            'no_warnings': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            audio_file = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
            logger.info(f"Downloaded audio to {audio_file}")
            fileName = audio_file.split("/")[-1].split(".")[0]
            return fileName