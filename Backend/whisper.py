import whisper
model = whisper.load_model("base")
result = model.transcribe("audio.file")  #need to change later to file name

transcribed_text = result["text"]

# print(transcribed_text)

with open("transcription.text" "w") as text_file:
    text_file.write(result["text"])
# a file in Backend called transcription.text will be created with the transcribed text inside

    
    
