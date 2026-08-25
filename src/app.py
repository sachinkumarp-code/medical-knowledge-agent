import streamlit as st
import requests
import os

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Medical AI", layout="centered")

# --- 2. ADVANCED CSS OVERRIDE ---
advanced_css = """
<style>
    /* Hide all default Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Clean up the main container width */
    .block-container {
        max-width: 850px;
        padding-top: 2rem;
        padding-bottom: 100px;
    }

    /* Strip chat bubble backgrounds and align text */
    .stChatMessage {
        background-color: transparent !important;
        border: none !important;
        padding: 1.5rem 0 !important;
        font-size: 1.05rem;
        line-height: 1.6;
    }

    /* Claude-style Floating Input Box */
    .stChatInputContainer {
        padding-bottom: 20px !important;
        background-color: transparent !important;
    }
    .stChatInputContainer > div {
        background-color: #1A1A1A !important;
        border: 1px solid #333333 !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.5) !important;
        padding: 4px;
    }
    
    /* Remove the default grey background from the user avatar */
    [data-testid="chatAvatarIcon-user"] {
        background-color: #333333 !important;
    }
    [data-testid="chatAvatarIcon-assistant"] {
        background-color: #111111 !important;
        color: #FFFFFF !important;
    }
</style>
"""
st.markdown(advanced_css, unsafe_allow_html=True)

# --- 3. THE HISTORY ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    # Using generic clean avatars instead of emojis
    st.chat_message(msg["role"]).write(msg["content"])

# --- 4. THE ACTION ---
user_input = st.chat_input("Message the Medical AI...")

if user_input:
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("Analyzing..."):
        try:
            API_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000/chat")
            response = requests.post(API_URL, json={"question": user_input})
            response.raise_for_status()
            
            ai_answer = response.json()["answer"]
            
        except Exception as e:
            ai_answer = f"**System Error:** Unable to connect to inference engine. ({e})"

    st.chat_message("assistant").write(ai_answer)
    st.session_state.messages.append({"role": "assistant", "content": ai_answer})