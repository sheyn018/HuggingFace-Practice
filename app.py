from dotenv import find_dotenv, load_dotenv
from transformers import pipeline

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)

    print(text)
    return text

img2text("https://cdn.britannica.com/86/166986-131-EE42A765/cute-kitten-and-puppy-outdoors-in-grass.jpg")