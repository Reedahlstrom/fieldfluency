import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="sk-...iFgA"




def get_feedback(prompt):
    response = client.chat.completions.create(
      model="gpt-4"
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
