# 🧮 Mirai Internship: Assignment 1

Welcome to **Assignment 1**! This project contains two Streamlit-based web applications that demonstrate clean UI design, Python interactivity, robust mathematical handling, and custom styling options.

---

## 📝 Project Description

This project consists of two distinct Streamlit scripts:
1. **Simple Greeting App (`app.py`)**: A introductory application that accepts a user's name and displays it dynamically when a button is clicked.
2. **Premium AI Calculator (`calculator.py`)**: A fully responsive, modern scientific calculator. It handles basic mathematical operations, advanced powers, modulo arithmetic, trigonometric calculations (Sine, Cosine, Tangent), and logarithmic evaluations. It also features custom dark-glassmorphism CSS styling, a persistent calculation history sidebar, and robust division-by-zero/error prevention.

---

## 🛠️ Tech Stack

*   **Programming Language**: Python 3.8+
*   **Web Framework**: Streamlit
*   **Styling**: Custom CSS & Glassmorphic UI design overrides
*   **Mathematical Operations**: Python `math` module

---

## 🧠 What I Learned

*   **Interactive Web Development**: Building web layouts completely in Python without writing verbose JavaScript/HTML boilerplate.
*   **State Management in Streamlit**: Utilizing `st.session_state` to implement a calculation history system that persists across page refreshes and interactions.
*   **Error Prevention**: Writing robust exception handlers for mathematical edge cases (e.g. division by zero, logarithmic constraints on non-positive numbers, undefined tangents, and numerical overflows).
*   **Custom Interface Styling**: Leveraging Streamlit's `unsafe_allow_html` parameter to inject professional typography and background gradients, elevating basic Streamlit pages into premium-feeling applications.

---

## 🚀 How to Use

Follow these steps to run the applications locally on your machine:

### 1. Prerequisites
Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).

### 2. Install Dependencies
Open your terminal/command prompt and install the required library:
```bash
pip install streamlit
```

### 3. Run the Applications
Navigate to the `Assignment_1` directory in your terminal and execute either of the following commands:

*   To run the **Greeting App**:
    ```bash
    streamlit run app.py
    ```
*   To run the **Premium Calculator**:
    ```bash
    streamlit run calculator.py
    ```

Streamlit will automatically launch the application in your default web browser (usually at `http://localhost:8501`).

---

## 📁 Folder Structure

```text
Assignment_1/
├── app.py             # Simple AI UI greeting application
├── calculator.py      # Premium scientific calculator application with custom CSS
└── README.md          # Comprehensive project documentation (this file)
```

---

## 🔮 Future Enhancements

*   **Graphing Functions**: Integrate `plotly` or `matplotlib` to render graphs dynamically based on equations.
*   **AI Helper**: Add a Gemini-powered chat widget to explain complex mathematical concepts or help solve equations.
*   **Matrix Algebra**: Add support for matrix operations (determinants, matrix multiplication).

---

## 🎓 Student and Internship Details

*   **Student Name**: Kanishka Pal
*   **Internship Program**: Mirai Internship
*   **Assignment Title**: Streamlit Basics & Calculator Enhancements
*   **Submission Date**: July 2026

---

## 🔒 License & Footer

Developed for academic/internship evaluation purposes.

***

<p align="center">
  Made with ❤️ by a Mirai Intern.
</p>
