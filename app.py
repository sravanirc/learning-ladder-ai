import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()
API_BASE = os.environ["ASTRA_API_BASE"]
FLOW_ID = os.environ["ASTRA_FLOW_ID"]
TOKEN = os.environ["ASTRA_TOKEN"]

API_URL = f"{API_BASE}/api/v1/run/{FLOW_ID}?stream=false"

st.title("Learning Ladder AI")
st.write("Plan. Learn. Achieve. With AI by your side.")

# Input fields
goal = st.text_input("Learning Goal", "")
duration = st.text_input("Duration (e.g., 4 weeks)", "4 weeks")
level = st.selectbox("Experience Level", ["beginner", "intermediate", "advanced"])

if st.button("Generate Plan"):
    # Astra API expects a single string in input_value
    user_prompt = f"""
    Goal: {goal}
    Duration: {duration}
    Experience level: {level}
    """

    payload = {
        "input_value": user_prompt,
        "output_type": "chat",
        "input_type": "chat"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    with st.spinner("Generating your learning plan..."):
        response = requests.post(API_URL, json=payload, headers=headers)
    print("Raw response:", response.text)

    if response.status_code == 200:
        try:
            data = response.json()
            # Extract the agent's response text
            result = data["outputs"][0]["outputs"][0]["results"]["message"]["data"]["text"]
            st.markdown(result)
        except Exception as e:
            st.error(f"Error parsing response: {e}")
    else:
        st.error(f"Error {response.status_code}: {response.text}")