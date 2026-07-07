import streamlit as st

st.title("My first AI UI")
st.write("This is my first mirai internship")

#User input
user_message= st.text_input("What is your name?")

if st.button("Button"):
    st.write(user_message)