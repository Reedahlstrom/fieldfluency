import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def get_feedback(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
