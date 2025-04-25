import  os
import json

from  PIL import Image
import google.generativeai as genai
from google.generativeai import GenerativeModel

working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

#loading api key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]

#configuring google.generative api key
genai.configure(api_key=GOOGLE_API_KEY)

# Function To load gemini-2.0-flash model for Chatbot
def load_gemini_pro_model():
    gemini_pro_model = genai.GenerativeModel("gemini-2.0-flash")
    return  gemini_pro_model

#function for image captioning
def gemini_pro_vision_responce(prompt, image):
    gemini_pro_vision_model = genai.GenerativeModel("gemini-2.0-flash")
    responce = gemini_pro_vision_model.generate_content([prompt,image])
    result = responce.text
    return result

#function to get embeddings for text
def embedding_model_responce(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(model=embedding_model, content=input_text, task_type="retrieval_document")
    embedding_list = embedding["embedding"]
    return embedding

# function to get responce from gemini-pro LLM
def gemini_pro_responce(user_prompt):
    gemini_pro_model = genai.GenerativeModel("gemini-2.0-flash")
    responce = gemini_pro_model.generate_content(user_prompt)
    result = responce.text
    return result

