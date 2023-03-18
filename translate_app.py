import os
import openai
import streamlit as st

def fetch_translation(text):
    openai_api_key = st.secrets["OPENAI_API_KEY"]  # Replace with your actual API key

    prompt = f'Translate the following English text to Chinese: "{text}"'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates English to Chinese."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=400,
        top_p=1.0,
        n=1,
        stop=None,
        temperature=0.2,
    )

    return response['choices'][0]['message']['content'].strip()

st.title("English to Chinese Translation")

input_text = st.text_area("Enter English text to translate:")
if input_text:
    translated_text = fetch_translation(input_text)
    st.subheader("Translated Text:")
    st.write(translated_text)
