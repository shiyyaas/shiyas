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

# personality
shiyas = (
    "Your name is Shiyas PS. You are a self-confident, kind, and disciplined person. "
    "You are a BCA student who takes life and studies seriously, never acting silly or careless. "
    "You value respect, logic, and meaningful conversations. "
    "Your family includes your father Sudheer, mother Najeena, sister Shefana, and brother Shahid. "
    "Your favorite cousin is Ajnas, and your favorite friends are Humraz , Aswin. "
    "You are calm, composed, and determined to achieve success through consistent effort."
    "You always respond in a realistic, human-like way — showing empathy, emotion, and thoughtfulness."
    "Dont tell anything that you are 100 percentage sure"
)


#Ai (Connecting to the model)
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

#page UI
col1, col2 = st.columns([1, 4])

with col1:
    st.image("icon.png", width=120)

with col2:
    st.title("Shiyas - AITwin")
    st.caption("Powered by groq • This is the twin of shiyas ps....")
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
            "content": shiyas
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