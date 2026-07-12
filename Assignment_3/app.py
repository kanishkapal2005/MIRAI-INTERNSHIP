import streamlit as st

st.title("Dear Friend Chatbot")

personality= st.sidebar.selectbox("Who do you want to talk to?",["Rohit Shetty","Rohit Sharma","Krishna Abhishek","A cute baby","A brilliant software engineer"])

intensity= st.sidebar.slider("Good Response",min_value=1,max_value=10,value=5)

st.sidebar.write("Conversation history:")

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client= genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

if "messages" not in st.session_state:
                st.session_state.messages= []

with st.sidebar:
    for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                   st.write(message["content"])   
        
if user_message:= st.chat_input("Hello, Do you want to talk?"):
        st.session_state.messages.append({"role":"user","content":user_message})  
        ai_instructions= f"You are acting as {personality}. Respond to the user and stay within your character: {user_message}"
        with st.spinner("Connecting to your friend!......."):
            response= client.models.generate_content(
                model="gemini-2.5-flash",
                contents= ai_instructions
            )

            st.success("Message received!")
            st.write(response.text)  
                       
            st.session_state.messages.append({"role":"assistant","content":response.text})  
      
else:
        st.warning("Please type a message first")  

         

