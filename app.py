# app.py
import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

#load the .env secret apikeys
# load_dotenv

#page informations
st.set_page_config(
    page_icon="icon.png",
    page_title="Chat with S-Bot",
    layout="centered"
)

#page UI
st.title("Shiyas - chatbot")
st.caption("Powered by Qwen • Ask me anything....")


with st.chat_message("user"):
    st.write("Hello!")

with st.chat_message("assistant"):
    st.write("Hi there!")

prompt = st.chat_input("Say something")

if prompt:
    st.write(f"You said: {prompt}")