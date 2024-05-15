from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI
import requests
import os
import streamlit as st

load_dotenv(find_dotenv())
HF_TOKEN = os.getenv("HF_TOKEN")
print(HF_TOKEN)

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)

    print(text)
    return text

def generate_story(scenario):
    template = """
    You are a story teller for kids. You are tasked to create a story based on the context below:
    
    Context: {scenario}

    Make a very short story that is suitable for kids.
    """

    prompt = PromptTemplate(
        template = template, 
        input_variables=["scenario"]
    )

    story_llm = LLMChain(
        llm = ChatOpenAI(
                model_name = 'gpt-3.5-turbo',
                temperature = 0.9,
            ),
            prompt = prompt,
            verbose = True
        )

    story = story_llm.run(scenario=scenario)
    print(story)
    return story

def text2speech(messsage):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": messsage
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open("audio.flac", "wb") as f:
        f.write(response.content)

def main():

    st.set_page_config(page_title="Story Generator", page_icon="📚", layout="wide")

    st.header("Story Generator")
    st.subheader("Generate a story for kids based on an image")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()

        with open(uploaded_file.name, "wb") as f:
            f.write(bytes_data)

        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        scenario = img2text(uploaded_file.name)
        story = generate_story(scenario)
        text2speech(story)

        with st.expander("Scneario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)

        st.audio("audio.flac")


if __name__ == "__main__":
    main()