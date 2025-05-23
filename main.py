import streamlit as st
from whisper_utils import transcribe_audio
from gpt_feedback import get_feedback

st.set_page_config(page_title="Field Fluency", layout="centered")

st.title("🩺 Field Fluency")
st.subheader("Practice your English speaking for the MET test")
st.markdown("Upload an audio response below to receive instant AI-powered feedback.")

audio_file = st.file_uploader("Upload audio (.mp3 or .wav)")

if audio_file:
    transcript = transcribe_audio(audio_file)
    st.write("📝 Transcript:")
    st.text_area("Transcript", value=transcript)

    if st.button("Get Feedback"):
        feedback = get_feedback(transcript)
        st.markdown("💬 **AI Feedback:**")
        st.write(feedback)

Add visible UI to main page

