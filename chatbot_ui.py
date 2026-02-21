import streamlit as st
import requests

st.set_page_config(page_title="Chatbot", layout="wide")

st.title("💬 Chatbot")
st.markdown("---")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })
    
    with st.chat_message("user"):
        st.markdown(user_input)
    
    # Generate bot response (placeholder)
    with st.chat_message("assistant"):
        response = f"Echo: {user_input}"
        st.markdown(response)
        
        # Add bot response to history
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

# Sidebar for settings
with st.sidebar:
    st.header("⚙️ Settings")
    st.write("Configure your chatbot here")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
