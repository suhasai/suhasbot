import os

from  PIL import Image
import streamlit as st
from streamlit import caption
from streamlit_option_menu import option_menu

import gemini_utility
from gemini_utility import gemini_pro_vision_responce
from gemini_utility import embedding_model_responce
from gemini_utility import gemini_pro_responce


working_directory = os.path.dirname(os.path.abspath(__file__))

#Setting up page configuration
st.set_page_config(
    page_title="Suhas AI Bot",
    page_icon="🐦‍🔥",
    layout="centered"
)

with st.sidebar:

    selected = option_menu("Gemini AI",["ChatBot", "Image Captioning", "Embed text", "Ask me anything"],menu_icon = 'robot', icons=['chat-dots-fill','image-fill','textarea-t','person raised hand'],default_index=0)

def translate_role_for_streamlit(user_role):
    if user_role == 'model':
        return  "assistant"
    else:
        return  user_role


if selected == "ChatBot":

    model = gemini_utility.load_gemini_pro_model()

    #initialise chat session in streamlit if not already presesnt
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])

    #streamlit page title
    st.title("🤖 ChatBot")

    #display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)


    #input field for users message
    user_prompt = st.chat_input("Ask GPT...")

    if user_prompt:
        st.chat_message("user").markdown(user_prompt)

        gemini_responce = st.session_state.chat_session.send_message(user_prompt)

        #display gemini-pro responce
        with st.chat_message("assistant"):
            st.markdown(gemini_responce.text)



# Image Captioning
if selected == "Image Captioning":
    st.title("📷 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg","png"])

    if st.button("Generate Caption"):

        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_image = image.resize((800, 600))
            st.image(resized_image)

        default_prompt = "Generate a caption for an Image"

        #getting responce from gemini-pro-vision model
        caption = gemini_pro_vision_responce(default_prompt, image)

        with col2:
            st.info(caption)


# text embedding page
if selected == "Embed text":

    st.title("🔠 Embed Text")

    # input text box
    input_text = st.text_area(label="", placeholder="Enter your text here")

    if st.button("get Embeddings"):
        responce = embedding_model_responce(input_text)
        st.markdown(responce)


# ask me a question
if selected == "Ask me anything":

    st.title(" ⁉️ Ask me Champ")

    #textbox to enter prompt by user
    user_prompt = st.text_area(label=" ", placeholder= "Enter your Prompt...")

    if st.button("Get Responce"):
        responce = gemini_pro_responce(user_prompt)
        st.markdown(responce)









