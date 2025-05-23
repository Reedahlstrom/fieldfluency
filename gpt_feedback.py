from openai import OpenAI

client = OpenAI(api_key="sk-...your_actual_api_key_here...")


def get_feedback(prompt):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
