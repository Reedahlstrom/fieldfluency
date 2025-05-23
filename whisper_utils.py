import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    with open("temp.wav", "wb") as f:
        f.write(audio_file.read())
    result = model.transcribe("temp.wav")
    return result["text"]
