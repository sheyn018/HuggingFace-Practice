from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import LLMChain, PromptTemplate
from langchain.chat_models import ChatOpenAI

load_dotenv(find_dotenv())

def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)

    print(text)
    return text



def generate_story(scenario):
    template = """
    You are a story teller for kids. You are tasked to create a story based on the context below:
    
    Context: {scenario}
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

scenario = img2text("https://cdn.britannica.com/86/166986-131-EE42A765/cute-kitten-and-puppy-outdoors-in-grass.jpg")
story = generate_story(scenario)
