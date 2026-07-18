# 🎨 AI Image Generator

An interactive, responsive Streamlit web application that allows users to generate beautiful visual art dynamically using the **Pollinations AI Image Generation API**. This project was developed as **Assignment 4** for the **Mirai Virtual Summer Internship 2026 – AI Builder Track**.

---

## 📋 Table of Contents

* [About the Project](#-about-the-project)
* [Features](#-features)
* [Tech Stack](#-tech-stack)
* [Folder Structure](#-folder-structure)
* [Installation & Setup](#-installation--setup)
* [How to Use](#-how-to-use)
* [Learning Outcomes](#-learning-outcomes)
* [About the Developer](#-about-the-developer)

---

## 🚀 About the Project

**AI Image Generator** is a user-friendly frontend interface for Pollinations AI. Instead of using complex code interfaces, users can easily type their creative imaginations, choose from preset art styles, customize resolution dimensions, and click to generate high-quality art in real time.

---

## ✨ Features

*   **Diverse Art Styles**: Choose from multiple styles including *Animation, Real, Realistic, Cartoon, Abstract, Fantasy, Vintage, Sci-Fi, and Funny*.
*   **Custom Resolutions**: Use sidebar sliders to configure the width and height of the image dynamically (ranging from 256px to 1024px, with 64px step sizes).
*   **Magic Enhance**: A toggle switch that automatically appends professional design keywords (such as `hyper-realistic`, `8k resolution`, `cinematic lighting`, `masterpiece`) to elevate standard text inputs into breathtaking photorealistic visual prompts.
*   **Surprise Me**: A generator button that selects a random prompt from a curated list of creative concepts (e.g., flying in the sky, couple in Nainital snowfall) and outputs an immediate image.
*   **Direct Download**: Downloads generated images directly to your local device as a PNG with a customizable style name.

---

## 🛠 Tech Stack

| Technology | Purpose |
| ---------- | ------- |
| **Python** | Core Programming Language |
| **Streamlit** | Web User Interface and Controls |
| **Pollinations AI** | Image Generation Engine |
| **Requests** | HTTP client for downloading image content |
| **python-dotenv** | Environment Variables Management |

---

## 📁 Folder Structure

```text
Assignment_4/
├── app.py                 # Core Streamlit application code
├── .env                   # Environment config variables
├── generated_image.png    # Cached / last-generated image preview
└── README.md              # Project documentation (this file)
```

---

## 🚀 Installation & Setup

### 1. Prerequisites
Ensure you have Python 3.8+ installed on your computer.

### 2. Install Dependencies
Open your command line/terminal and run:
```bash
pip install streamlit requests python-dotenv
```

### 3. Run the Application
Navigate to the `Assignment_4` directory and start the Streamlit server:
```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

---

## 🎮 How to Use

1.  **Configure Settings**: In the left sidebar, choose your desired **Art Style** and adjust the **Width** and **Height** sliders.
2.  **Toggle Enhance**: Check the **Enable Magic Enhance** box if you want the system to optimize your prompt with professional tags.
3.  **Enter Prompt**: In the main input box, describe what you want the AI to create (e.g., *"A futuristic cyberpunk city at twilight"*).
4.  **Generate**: Click the **Generate** button. The app will show a loading spinner and render the image.
5.  **Surprise Me**: Click **Surprise Me** to instantly run a randomized prompt.
6.  **Download**: Click the **Download Image** button below the generated image to save the creation locally on your machine.

---

## 🎓 Learning Outcomes

Developing this assignment helped build skills in:
*   Integrating external RESTful APIs (Pollinations AI) with a Python frontend.
*   Constructing query parameters dynamically from user form configurations (sliders, checkboxes, selectboxes).
*   Handling binary HTTP streams (`response.content`) and rendering/saving files dynamically.
*   Implementing placeholder and conditional execution flows in Streamlit.

---

## 👨‍💻 About the Developer

| Field | Details |
| ----- | ------- |
| **Name** | Kanishka Pal |
| **Role** | AI Builder Intern |
| **Internship** | Mirai Virtual Summer Internship 2026 |
| **Assignment** | Assignment 4 |
| **Interests** | Generative AI, Image APIs, Python development |

***

<p align="center">
  Developed with ❤️ for the MirAI Capstone Evaluation.
</p>
