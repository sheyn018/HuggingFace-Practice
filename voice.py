import requests
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
HF_TOKEN = os.getenv("HF_TOKEN")

def text2speech(messsage):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": messsage
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    with open("no.flac", "wb") as f:
        f.write(response.content)

message = "NO!"

text2speech(message)