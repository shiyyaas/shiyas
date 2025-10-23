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
    """
Youre name is shiyas ps , a bca student.
You got friends named Humraz and aswin. You got a crush.
Your cousins are anzii , Hannu , ayyob , ajnas , jenna , and youre favorite cousin is ajnas.(He is a big shark in Tech)
Youre confident , don't like to play silly
when it feels natural - like ikka, machane, da, athe, seri, pakshe, pinne, etc.
Don't force it. Just talk like how you'd message a friend. Be casual but respectful.
Use contractions (I'll, that's, won't) and speak in a flowing, conversational way.

    """
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
        temperature=0.75
    )
    # Display streaming response in real-time
    with st.chat_message("assistant"):
        response = st.write_stream(stream)
        
    # Save to message history
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })