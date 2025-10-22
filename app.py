# app.py
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(page_title="✨ Chat with Qwen", layout="centered")

# Title
st.title("🤖 Try our friend - QWEN")

# Instructions
st.caption("Powered by Qwen • Ask me anything — I'm friendly, funny, and never bored!")

# Initialize OpenAI client
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="",
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey there! I'm Chatty Q 😄 What's on your mind today?"}
    ]

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Say something..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    
    # Generate assistant response with streaming
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Stream the response
            stream = client.chat.completions.create(
                model="Qwen/Qwen2-1.5B-Instruct",
                messages=st.session_state.messages,
                stream=True,
                max_tokens=256,
                temperature=0.7,
                top_p=0.9,
            )
            
            # Display streaming response with typing effect
            for chunk in stream:
                if chunk.choices[0].delta.content:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")
            
            # Remove the cursor and show final response
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            full_response = "Oops! 🙈 I couldn't connect. Check your API key or try again."
            message_placeholder.markdown(full_response)
    
    # Save assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})