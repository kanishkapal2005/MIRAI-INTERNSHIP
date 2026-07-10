import streamlit as st

st.title("Dear Friend Chatbot")

personality= st.sidebar.selectbox("Who do you want to talk to?",["Rohit Shetty","Rohit Sharma","A cute baby","A brilliant software engineer"])

intensity= st.sidebar.slider("Good Response",min_value=1,max_value=10,value=5)

from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client= genai.Client(api_key= os.getenv("GEMINI_API_KEY"))

user_message= st.text_input("Hello, Do you want to talk?")
if st.button("Send"):
    if user_message:
        ai_instructions= f"You are acting as {personality}. Respond to the user and stay within your character: {user_message}"
        with st.spinner("Connecting to your friend!......."):
            response= client.models.generate_content(
                model="gemini-2.5-flash",
                contents= ai_instructions
            )

            st.success("Message received!")
            st.write(response.text)

    else:
        st.warning("Please type a message first")       