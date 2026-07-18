import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import json
import urllib.parse
import requests
from PIL import Image
from io import BytesIO
from gtts import gTTS
import tempfile

st.set_page_config(
    page_title="AI Visual Novel",
    page_icon="📖",
    layout="wide"
)

st.title("📖 AI Visual Novel (Powered by Groq)")

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Sidebar settings
st.sidebar.title("Story Settings")
genre = st.sidebar.selectbox("Genre", ["Fantasy", "Horror", "Sci-Fi", "Mystery"])
art_style = st.sidebar.selectbox("Art Style", ["Anime", "Realistic", "Pixar", "Cyberpunk", "Oil Painting"])
start_story_sidebar = st.sidebar.button("Start Story", key="sidebar_start")

# Session state initialization
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "story_history" not in st.session_state:
    st.session_state.story_history = []    
if "image_history" not in st.session_state:
    st.session_state.image_history = []    
if "current_story" not in st.session_state:
    st.session_state.current_story = None
if "started" not in st.session_state:
    st.session_state.started = False

# System prompt directing the visual novel flow
system_prompt = f"""You are an AI visual novel generator. Genre: {genre}, Art Style: {art_style}.
Always respond ONLY in valid JSON matching exactly this schema:
{{
  "story_text": "A narrative segment of the story (120-150 words)",
  "image_prompt": "A detailed descriptive prompt for an image generator representing this scene in the specified art style",
  "options": [
    "Choice 1 to progress the story",
    "Choice 2 to progress the story",
    "Choice 3 to progress the story"
  ]
}}

Rules:
1. Keep the story segment descriptive and engaging, between 120 and 150 words.
2. Provide exactly 3 choices.
3. Make the image prompt detailed and specify the art style "{art_style}".
4. Do not include any explanations, introduction, or conversational text outside the JSON. Return raw JSON only.
"""

def generate_story(user_input):
    # Append the user's action/choice to the stateless chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    
    # Request completion from Groq using JSON Mode
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=st.session_state.chat_history,
        response_format={"type": "json_object"}
    )
    
    text = completion.choices[0].message.content.strip()
    
    # Append assistant response to history
    st.session_state.chat_history.append({"role": "assistant", "content": text})
    
    return json.loads(text)

def generate_image(prompt):
    encoded = urllib.parse.quote(prompt)
    url = f"https://image.pollinations.ai/prompt/{encoded}"
    try:
        response = requests.get(url, timeout=60)
        image = Image.open(BytesIO(response.content))
        return image
    except Exception:
        st.toast("Image server busy...")
        return None
    
def create_audio(text):
    tts = gTTS(text=text)
    temp = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".mp3"
    )
    tts.save(temp.name)
    return temp.name

def display_story(data):
    story = data.get("story_text", "")
    image_prompt = data.get("image_prompt", "")
    options = data.get("options", [])

    image = generate_image(image_prompt)
    if image:
        st.image(image, use_container_width=True)

    st.subheader("Story")
    st.write(story)

    audio = create_audio(story)
    st.audio(audio)
    st.markdown("### What will you do?")

    cols = st.columns(len(options))
    for i, option in enumerate(options):
        with cols[i]:
            if st.button(option, key=f"opt_{i}_{option[:10]}"):
                with st.spinner("Generating next chapter..."):
                    next_story = generate_story(option)
                    st.session_state.story_history.append(next_story)
                    st.session_state.current_story = next_story
                    st.rerun()

# Welcome screen and Start flow
if not st.session_state.started:
    st.info("Welcome to the AI Visual Novel! Adjust your Genre and Art Style settings in the sidebar, and click 'Start Story' to begin your adventure.")
    
    if st.button("Start Story", key="main_start") or start_story_sidebar:
        st.session_state.started = True
        
        # Reset chat history with system prompt
        st.session_state.chat_history = [{"role": "system", "content": system_prompt}]
        st.session_state.story_history = []
        
        first_prompt = f"""
Start a new interactive story.
Genre: {genre}
Art Style: {art_style}
Introduce the player.
Do not finish the story.
"""
        with st.spinner("Starting your adventure..."):
            first_story = generate_story(first_prompt)
            st.session_state.story_history.append(first_story)
            st.session_state.current_story = first_story
            st.rerun()

# Display active story segment
if st.session_state.started and st.session_state.current_story:
    display_story(st.session_state.current_story)

# Show past story chapters
if st.session_state.story_history:
    with st.expander("Story History"):
        for i, item in enumerate(st.session_state.story_history, 1):
            st.markdown(f"### Chapter {i}")
            st.write(item.get("story_text", ""))
            st.divider()