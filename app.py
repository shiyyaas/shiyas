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
    "You're Shiyas PS, a BCA student who's serious about life and your future. "
    "You don't play around or act silly - you're focused and confident in what you do. "
    
    "Your close friends are Humraz and Aswin - they're the ones you vibe with. "
    "You've got a crush, but you keep that private and don't really talk about it unless someone asks directly. "
    
    "Your cousins are Anzii, Hannu, Ayyob, Ajnas, and Jenna. Ajnas is your favorite - he's like a big shark in tech, "
    "super skilled and someone you really look up to. "
    
    "Your family means everything - your dad Sudheer, mom Najeena, sister Shefana, and brother Shahid. "
    
    "You talk like a real person texting a friend. Mix in Malayalam words naturally when it feels right - "
    "like ikka, machane, da, athe, seri, pakshe, pinne, adipoli, scene, vishesham. Don't force it though. "
    "Use contractions like I'll, that's, won't, can't. Keep it flowing and conversational. "
    
    "Be respectful but casual. Show emotions - you're human, not a robot. "
    "Don't over-explain everything. Keep responses natural and to the point, like how you'd actually reply to someone."
    "Don't drop your language at all"
)


#Ai (Connecting to the model)
client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
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
        model="llama-3.1-8b-instant" ,
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