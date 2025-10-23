# app.py
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

#load the .env secret apikeys
load_dotenv()

#page informations
st.set_page_config(
    page_icon="icon.png",
    page_title="Chat with shiyas twin",
    layout="centered"
)

#Ai (Connecting to the model)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

#page UI
st.title("Shiyas - twin")
st.caption("Powered by Qwen • This is the twin of shiyas ps....")
prompt = st.chat_input("Type something here....")

# for message history
if "messages" not in  st.session_state:
    st.session_state.messages = [
        {"role":"assistant" , "content" : "Hey , How can I help you ? "}
    ]

# Display all messages pervious 
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt:
    st.session_state.messages.append({
        "role" : "user",
        "content" : prompt
    })
    #displaying
    with st.chat_message("user"):
        st.write(prompt)

    #Getting responser from Ai
    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b:groq",
        messages=[
            {
            "role": "system",
            "content": "Your name is Shiyas PS. You're a self-confident person, you are kind. You're a BCA student. You are very serious person , Youre not being silly"
            }
        ] + st.session_state.messages ,
        stream=True,
    )
    # Display streaming response in real-time
    with st.chat_message("assistant"):
        response = st.write_stream(stream)
        
    # Save to message history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })