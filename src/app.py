import streamlit as st
import requests
import os

st.title("Medical AI Assistant")

# 1. The Setup: Create the memory box if it doesn't exist yet
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. The History: Print all past messages onto the screen
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# 3. The New Action: Wait for the user to type something at the bottom
user_input = st.chat_input("Ask medical or patient question")

if user_input:
    # Print and save the user's question
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Send it to your FastAPI backend
    API_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000/chat")
    response = requests.post(API_URL, json={"question": user_input})
    ai_answer = response.json()["answer"]
    
    # Print and save the AI's answer
    st.chat_message("assistant").write(ai_answer)
    st.session_state.messages.append({"role": "assistant", "content": ai_answer})