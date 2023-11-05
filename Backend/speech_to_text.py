import openai
import os
openai.api_key = "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"
audio_file = open("PLACE_HOLDER", "rb")  #This is a placeholder for the eventual file that should be rendered every 30 seconds of the real-time live stream 

transcript = openai.Audio.transcribe("whisper-1", audio_file) 

print(transcript)

with open(os.path.join(os.getcwd(), "transcription.txt"), "w") as text_file:
    text_file.write(transcript["text"])
