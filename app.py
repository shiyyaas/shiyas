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
    page_title="Chat with S-Bot",
    layout="centered"
)

#Ai (Connecting to the model)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

#page UI
st.title("Shiyas - chatbot")
st.caption("Powered by Qwen • Ask me anything....")
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
    #Getting responser from Ai
    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b:groq",
        instructions="Youre name is shiyas ps , youre a self confident person , you are kind , Youre a bca student",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        stream=True,
    )
    #Saving to response to messages(history)
    response = ""
    for chunk in stream:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
    st.session_state.messages.append({
        "role" : "user" ,
        "content" : response
    })