# The MULTIVERSE OF CHATBOTS

An interactive AI chatbot application built using **Streamlit** and **Google Gemini 2.5 Flash**. This project was developed as **Assignment 2** for the **Mirai Virtual Summer Internship 2026 – AI Builder Track**.

The application allows users to interact with multiple AI personalities, each responding completely in character, creating a fun and engaging conversational experience.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-FF4B4B?style=flat-square\&logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-blue?style=flat-square\&logo=google)

---

# 📋 Table of Contents

* About the Project
* Features
* Tech Stack
* Project Workflow
* Installation & Setup
* How to Use
* Learning Outcomes
* Future Enhancements
* About the Developer
* References

---

# 🚀 About the Project

**The MULTIVERSE OF CHATBOTS** is a personality-driven AI chatbot built using **Streamlit** and the **Google Gemini API**.

Instead of talking to a generic chatbot, users can choose from multiple unique personalities and receive responses that remain completely in character throughout the conversation.

Available personalities include:

* 💻 An Expert Hacker
* 🏏 An Angry Ravi Shastri
* ⚽ A Crazy Ronaldo Fan
* 🇺🇸 Donald Trump

The selected personality is combined with the user's message and sent to **Gemini 2.5 Flash**, which generates a response while maintaining the chosen character.

This assignment introduces prompt engineering, API integration, and AI-powered application development using Python.

---

# 🛠 Tech Stack

| Technology              | Purpose                         |
| ----------------------- | ------------------------------- |
| Python 3.10+            | Core Programming Language       |
| Streamlit               | User Interface                  |
| Google Gemini 2.5 Flash | AI Response Generation          |
| python-dotenv           | Environment Variable Management |
| Google GenAI SDK        | Gemini API Client               |

---

# ✨ Features

## 🎭 Multiple AI Personalities

Users can select different virtual personalities before starting a conversation.

Current personalities include:

* Expert Hacker
* Angry Ravi Shastri
* Crazy Ronaldo Fan
* Donald Trump

---

## 💬 Interactive Chat

Users simply type a message and click **SEND** to receive an AI-generated response.

---

## 🧠 Prompt Engineering

Each user message is automatically transformed into a structured prompt:

> "You are acting as {selected personality}. Respond to the user's message while staying completely in character."

This ensures every response matches the selected personality.

---

## ⚡ Google Gemini Integration

The application connects to **Gemini 2.5 Flash** using the official Google GenAI Python SDK.

Responses are generated in real time using Google's latest AI model.

---

## 🔐 Secure API Key Management

The Gemini API key is stored inside a `.env` file and loaded securely using `python-dotenv`.

No API keys are hardcoded into the application.

---

## ⏳ Loading Animation

While waiting for the AI response, Streamlit displays:

> Connecting to the multiverse!......

This provides a better user experience.

---

## ✅ Success & Validation

The application handles common user interactions gracefully:

* Displays a success message after receiving the AI response.
* Warns the user if the message box is empty.
* Prevents unnecessary API requests.

---

# 🔄 Project Workflow

```text
User Opens App
        │
        ▼
Select Personality
        │
        ▼
Enter Message
        │
        ▼
Click SEND
        │
        ▼
Create AI Prompt
        │
        ▼
Send Request to Gemini API
        │
        ▼
Generate Response
        │
        ▼
Display AI Reply
```

---

# 🚀 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/multiverse-of-chatbots.git

cd multiverse-of-chatbots
```

---

## 2. Create a Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

macOS/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit

pip install google-genai

pip install python-dotenv
```

---

## 4. Create a `.env` File

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## 5. Run the Application

```bash
streamlit run app.py
```

The application will launch at:

```
http://localhost:8500
```

---

# 🎮 How to Use

1. Launch the application.
2. Select an AI personality.
3. Type your message.
4. Click **SEND**.
5. Wait while the app connects to Gemini.
6. Read the AI-generated response.

---

# 🎓 Learning Outcomes

This assignment helped develop practical skills in:

* Streamlit application development
* Google Gemini API integration
* Prompt engineering
* Environment variable management
* Python package management
* API request handling
* User input validation
* AI-powered application development

---

# 🔮 Future Enhancements

* Conversation history
* Chat memory
* Custom personality creation
* Voice input and speech output
* Image generation support
* Dark/Light theme toggle
* Export chat as PDF
* Multi-language conversations

---

# 👨‍💻 About the Developer

| Field      | Details                                                                              |
| ---------- | ------------------------------------------------------------------------------------ |
| Name       | Kanishka Pal                                                                           |
| Role       | AI Builder Intern                                                                    |
| Internship | Mirai Virtual Summer Internship 2026                                                 |
| Assignment | Assignment 2                                                                         |
| Interests  | Artificial Intelligence, Machine Learning, Python, Streamlit, Full Stack Development |

---

# 📚 References

* Streamlit Documentation — https://docs.streamlit.io/
* Google GenAI Python SDK — https://googleapis.github.io/python-genai/
* Google AI for Developers (Gemini API) — https://ai.google.dev/
* Python Documentation — https://docs.python.org/3/
* python-dotenv Documentation — https://pypi.org/project/python-dotenv/

---

# 📜 License

Developed for the **Mirai Virtual Summer Internship 2026 – AI Builder Track**.

© 2026 Aman Gupta. All rights reserved.