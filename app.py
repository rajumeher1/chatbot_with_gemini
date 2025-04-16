import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
import os

# Load the .enve enviroment
load_dotenv()


# Access the API key form the .env file
key = os.getenv('GEMINI_API_KEY')


# Configure the generative model
genai.configure(api_key=key)


# Function to initiate the gemini model and get the response
def get_gemini_response(question):

    #Load the Model
    model = genai.GenerativeModel(model_name='gemini-2.0-flash-lite')

    #get the response
    response = model.generate_content(question)

    return response.text

# Intitiate the Streamlit application

st.set_page_config(page_title='Chatbot', layout='centered')

st.subheader('Chatbot with Gemini')

if 'history' not in st.session_state:
    st.session_state.history = []

input_text = st.chat_input('Ask Anything')

if input_text:
    answer = get_gemini_response(input_text)

    st.session_state.history.append({'input': input_text, 'answer': answer})

for chat in st.session_state.history:
    st.markdown(f"**:orange[You : ]**  \n{chat['input']}")
    st.markdown(f"**:green[Gemini : ]**  \n{chat['answer']}")