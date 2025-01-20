from pipelien.download_and_transcript import Stage_download_video, Stage_Transcribe,Stage_generate_audio


STAGE_NAME  = "Download_YT_Video"
p = Stage_download_video()
filename = p.main()


STAGE_NAME = "Transcribe_YT_Video"
p = Stage_Transcribe(filename="raw_1")
filename = p.main()

STAGE_NAME = "Generate _audio_from_text"
p = Stage_generate_audio(filename)
p.main()




