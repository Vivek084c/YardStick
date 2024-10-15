from stages import Stage_01_YT_download
from stages.Stage_01_YT_download import yt_download
from stages.Stage_02_audio_to_text import cvt_audio_to_text
from stages.Stage_03_text_to_audio import cvt_text_to_audio
from src.Log import logger
import asyncio
from utils.utils_1 import save_to_file


class Stage_download_video:
    def __init__(self) -> None:
        pass
    def main(self):
        logger.info("Created yt_download instace")
        download = yt_download()
        logger.info("Started downloading the Yt video")
        filename = download.Download_YT_video()
        logger.info("Download compleated")
        return filename

class Stage_Transcribe:
        def __init__(self, filename):
            self.filename = filename
        def main(self):
            logger.info("Created Transcriber Object")
            c = cvt_audio_to_text(filename=self.filename)
            text_outfile = asyncio.run(c.Convert_to_text())
            logger.info("Transcribing process completed")
            save_to_file(self.filename, text_outfile)
            logger.info(f"file saved as {self.filename}")
            return self.filename
        
class Stage_generate_audio:
    def __init__(self,filename) -> None:
        self.filename = filename
    def main(self):
        logger.info("Created Audion generation object")
        c = cvt_text_to_audio(filename=self.filename)
        c.Covnert_text_to_audio()
        logger.info("Compleated audio generation")
        



        


    



