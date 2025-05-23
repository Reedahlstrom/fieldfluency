import openai

import streamlit as st
openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_feedback(text):
    prompt = f"""
You are a language coach helping a nurse prepare for the MET English exam. Here is their spoken response:

"{text}"

Correct any grammar errors. Suggest two better ways to say key phrases. Rate fluency 1–5 with reasoning.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']
