import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Page and theme
st.set_page_config(page_title="Learning Ladder AI", layout="wide")

# Load environment variables
load_dotenv()
API_BASE = os.environ["ASTRA_API_BASE"]
FLOW_ID = os.environ["ASTRA_FLOW_ID"]
TOKEN = os.environ["ASTRA_TOKEN"]
API_URL = f"{API_BASE}/api/v1/run/{FLOW_ID}?stream=false"

# Custom CSS for colors and layout
st.markdown(
    """
    <style>
    .block-container {
        background-color: #FAFAF7;
        border-radius: 12px;
        padding: 2rem;
        max-width: 900px;
        margin: auto;
    }
 
    div.stButton > button:first-child {
        background-color: #008080;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        height: 3rem;
        width: 100%;
    }
    div.stButton > button:hover {
        background-color: #FF6F61;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================================
# ROW 1: Title
# ================================
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: #008080; margin-bottom: 0;'>Learning Ladder AI</h1>
        <h5 style='color: #FF6F61; font-style: italic; margin-top: 0.5rem;'>
            Plan. Learn. Achieve. With AI by your side.
        </h5>
    </div>
  
    """,
    unsafe_allow_html=True
)
# ================================
# ROW 2: Inputs
# ================================

st.markdown(
    """
    <style>
    .compact-row {
        margin-top: 0.25rem;
        margin-bottom: 1.5rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style="
        text-align: center;
        width: full;
        margin: 0.2rem auto 1rem auto;
        color: #333333;
        font-size: 1rem;
        line-height: 1.5;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    ">
        Welcome to Learning Ladder AI, your personal AI-powered study companion designed to help you plan and achieve your learning goals efficiently.
        Simply enter the topic you want to learn,your preferred study duration, and experience level below, then click “Generate Plan” to receive a customized learning roadmap tailored just for you.
    </p>
    """,
    unsafe_allow_html=True
)
col1, col2, col3, col4 = st.columns([1, 1, 1, 1], gap="medium")

with col1:
    goal = st.text_input("Topic", placeholder="e.g., Learn Jest")

with col2:
    duration = st.text_input("Duration", value="4 weeks")

with col3:
    level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

with col4:
    st.write("")  # spacing to align button vertically
    generate = st.button("Generate Plan", use_container_width=True)

# ================================
# ROW 3: Results
# ================================
if generate:
   
    user_prompt = f"Goal: {goal}\nDuration: {duration}\nExperience level: {level}"
    payload = {
        "input_value": user_prompt,
        "output_type": "chat",
        "input_type": "chat"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    with st.spinner("Generating your personalized plan..."):
        response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            result = data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]

            st.markdown("## Your Learning Plan")
            st.markdown(result)

        except Exception as e:
            st.error(f"Error parsing response: {e}")
    else:
        st.error(f"Error {response.status_code}: {response.text}")
else:
    st.info("Enter details above and click **Generate Plan**.")
