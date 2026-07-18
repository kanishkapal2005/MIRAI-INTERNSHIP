import streamlit as st
import requests
from dotenv import load_dotenv
load_dotenv()
from google import genai
import os
from turtle import width
import random
import urllib.parse

st.title("AI IMAGE GENERATOR")

st.sidebar.header("Settings")
Type= st.sidebar.selectbox("Select the image type you want",["Animation","Real","Realistic","Cartoon","Abstract","Fantasy","Vintage","Sci-Fi","Funny"])
width=st.sidebar.slider("Width",max_value=1024,min_value=256,value=512,step=64)
height=st.sidebar.slider("Height",max_value=1024,min_value=256,value=512,step=64)

Magic= st.sidebar.checkbox("Enable Magic Enhance")
user_input= st.text_input("Create your imagination")
surprise_prompts=["A simple girl is flying in the sky like a bird","Two dogs are fighting","A couple is enjoying in the snowfall in nainital" ]
col1,col2= st.columns(2)
with col1:
 generate_btn= st.button("Generate")
with col2:
    surprise_btn= st.button("Surprise Me")
if user_input:
         with st.spinner("Creating your image....."):
          def enhance_prompt(user_input):
               secret_modifiers= ("hyper-realistic, 8k resolution, highly detailed, cinematic lighting,""masterpiece,photorealistic, vivid colors, trending on artstation")
               return f"{user_input}{secret_modifiers}"
          if Magic:
               final_prompt= enhance_prompt(user_input)
          else:
               final_prompt= user_input  
              
          assistant_command= f'{final_prompt},make the art style: {Type} style, {width}*{height} resolution'
          url = f"https://image.pollinations.ai/prompt/{assistant_command}?width={width}&height={height}"
          response=requests.get(url)
          st.image(response.content)

          if response.status_code==200:
                image_filename= "generated_image.png"
                with open(image_filename,"wb") as f:
                    st.download_button(label="Download Image",data= response.content,file_name="{Type}_image.png",mime="image/png")
                    st.success("Image successfully generated")

            
if generate_btn:
      if user_input.strip():
            st.session_state.surprise.btn= None
            st.image(response.content)
      else:
            st.warning("Please enter a prompt first")      
if surprise_btn:
      random_prompt= random.choice(surprise_prompts)
      st.session_state.surprise_prompt= random_prompt
      with st.spinner("Connecting to thr result....."):
        url = f"https://image.pollinations.ai/{random_prompt}?width={width}&height={height}"
        surprise_response=requests.get(url)
        st.image(surprise_response.content)


            
        