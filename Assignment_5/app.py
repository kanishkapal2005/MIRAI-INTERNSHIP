import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
st.title("CHATBOT WITH HISTORY")

def google_api(){
    return genai.Client(api_key= os.getenv("API_KEY"))
}

client= google_api()

user_input= st.text_input("Hello, Do you want to talk?")
if "messages" not in st.session_state:
    st.session_state.messages=[]

if "gemini_chat" not in st.session_state:
    st.sesson_state.gemini_chat= user_input

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])        
if user_message:= st.chat_input("Say something"):

    with st.chat_message(message["user"]):
        st.write(message["user_message"])        

    st.session_state.messages.append({"role":"user","content":user_message})    

    with st.spinner("Thinking...."):
        response=st.session_state.gemini_chat.send_message(user_message)

    with st.chat_message(message["AI"]):
        st.write(message["response.text"])    
    st.session_state.messages.append({"role":"AI","content":response.content})

    # Create a new string -> text
    #USE A LOOP AND ITERATE OVER THE MESSAGES
