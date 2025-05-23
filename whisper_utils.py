import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    with open("uploaded_audio.wav", "wb") as f:
        f.write(audio_file.read())
    
    result = model.transcribe("uploaded_audio.wav")
    return result["text"]
