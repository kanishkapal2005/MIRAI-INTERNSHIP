import streamlit as st
import math

# Set page config for a premium browser tab title and layout
st.set_page_config(
    page_title="Premium AI Calculator",
    page_icon="🧮",
    layout="centered"
)

# Premium Custom CSS Styling for a dark/glassmorphic interface
st.markdown("""
<style>
/* Modern fonts and backdrop */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Outfit', sans-serif;
    background: radial-gradient(circle at top right, #1f1b2e, #0d0b14);
    color: #e0e0ff;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #12101f;
    border-right: 1px solid rgba(255, 255, 255, 0.05);
}

/* Header style */
h1 {
    font-weight: 700;
    background: linear-gradient(45deg, #00ffcc, #0099ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0px 4px 20px rgba(0, 255, 204, 0.15);
    margin-bottom: 25px;
}

/* Subtitle and radio label styling */
.stMarkdown p, label {
    color: #b0afca !important;
    font-weight: 500 !important;
}

/* Buttons style */
div.stButton > button:first-child {
    background: linear-gradient(135deg, #00ffcc 0%, #0099ff 100%);
    color: #0b0914 !important;
    font-weight: 600;
    font-size: 16px;
    border-radius: 8px;
    border: none;
    padding: 12px 30px;
    box-shadow: 0 4px 15px rgba(0, 255, 204, 0.3);
    transition: all 0.3s ease-in-out;
    width: 100%;
}

div.stButton > button:first-child:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 255, 204, 0.5);
    color: #0b0914 !important;
}

div.stButton > button:first-child:active {
    transform: translateY(1px);
}

/* Glassmorphism card for results */
.result-card {
    background: rgba(255, 255, 255, 0.03);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 24px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4);
    margin-top: 25px;
    text-align: center;
}

.result-title {
    color: #8f8daf;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.result-val {
    color: #00ffcc;
    font-size: 32px;
    font-weight: 700;
    text-shadow: 0 0 15px rgba(0, 255, 204, 0.3);
}

.result-expr {
    color: #b0afca;
    font-size: 16px;
    margin-top: 5px;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 Premium AI Calculator")
st.write("A beautifully designed scientific calculator with state tracking and error handling.")

# Available mathematical operations
operations = [
    "Addition",
    "Subtraction",
    "Multiplication",
    "Division",
    "Exponentiation (Power)",
    "Modulo",
    "Square Root",
    "Logarithm (Natural)",
    "Logarithm (Base 10)",
    "Sine",
    "Cosine",
    "Tangent"
]

operation = st.selectbox("Choose operation you want to perform:", operations)

# Operations that only require a single input value
single_input_ops = [
    "Square Root",
    "Logarithm (Natural)",
    "Logarithm (Base 10)",
    "Sine",
    "Cosine",
    "Tangent"
]

# User inputs
st.write("---")
n1 = st.number_input("Enter your 1st number (or value of x):", value=0.0, format="%.6f")

if operation not in single_input_ops:
    n2 = st.number_input("Enter your 2nd number (or power/divisor):", value=0.0, format="%.6f")
else:
    n2 = 0.0

# Initialize calculation history in session state
if 'history' not in st.session_state:
    st.session_state.history = []

result = None
error_msg = None
expr_string = ""

# Calculation logic
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = n1 + n2
            expr_string = f"{n1} + {n2}"
        elif operation == "Subtraction":
            result = n1 - n2
            expr_string = f"{n1} - {n2}"
        elif operation == "Multiplication":
            result = n1 * n2
            expr_string = f"{n1} × {n2}"
        elif operation == "Division":
            if n2 == 0:
                error_msg = "Error: Division by zero is not allowed."
            else:
                result = n1 / n2
                expr_string = f"{n1} ÷ {n2}"
        elif operation == "Exponentiation (Power)":
            result = math.pow(n1, n2)
            expr_string = f"{n1} ^ {n2}"
        elif operation == "Modulo":
            if n2 == 0:
                error_msg = "Error: Modulo by zero is not allowed."
            else:
                result = n1 % n2
                expr_string = f"{n1} % {n2}"
        elif operation == "Square Root":
            if n1 < 0:
                error_msg = "Error: Square root of a negative number is not defined in real numbers."
            else:
                result = math.sqrt(n1)
                expr_string = f"√({n1})"
        elif operation == "Logarithm (Natural)":
            if n1 <= 0:
                error_msg = "Error: Logarithm is only defined for positive numbers."
            else:
                result = math.log(n1)
                expr_string = f"ln({n1})"
        elif operation == "Logarithm (Base 10)":
            if n1 <= 0:
                error_msg = "Error: Logarithm is only defined for positive numbers."
            else:
                result = math.log10(n1)
                expr_string = f"log₁₀({n1})"
        elif operation == "Sine":
            result = math.sin(math.radians(n1))
            expr_string = f"sin({n1}°)"
        elif operation == "Cosine":
            result = math.cos(math.radians(n1))
            expr_string = f"cos({n1}°)"
        elif operation == "Tangent":
            # Check if tangent is undefined (90, 270, -90, etc. in degrees)
            if math.isclose((n1 - 90) % 180, 0, abs_tol=1e-9):
                error_msg = f"Error: Tangent of {n1}° is undefined."
            else:
                result = math.tan(math.radians(n1))
                expr_string = f"tan({n1}°)"
    except OverflowError:
        error_msg = "Error: Result is too large (numerical overflow)."
    except Exception as e:
        error_msg = f"Error: {str(e)}"

    # If result was calculated successfully, save to history
    if result is not None:
        # Check if the result is an integer equivalent, format nicely
        if result.is_integer() if isinstance(result, float) else False:
            formatted_res = int(result)
        else:
            formatted_res = round(result, 6)
            
        history_item = f"{expr_string} = {formatted_res}"
        st.session_state.history.append(history_item)
        
        # Display output card
        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">Calculation Successful</div>
            <div class="result-val">{formatted_res}</div>
            <div class="result-expr">{expr_string}</div>
        </div>
        """, unsafe_allow_html=True)
    elif error_msg:
        st.error(error_msg)

# Calculation History sidebar
st.sidebar.title("🕒 Calculation History")
if st.sidebar.button("Clear History"):
    st.session_state.history = []
    st.sidebar.success("History cleared!")

if st.session_state.history:
    for idx, item in enumerate(reversed(st.session_state.history)):
        st.sidebar.markdown(f"**{idx + 1}.** `{item}`")
else:
    st.sidebar.info("No calculations in this session yet.")

