#Getting all libraries
import getpass
import streamlit as st
import os
import json
from dotenv import load_dotenv, find_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
load_dotenv(find_dotenv(), override=True)

#Initializing History
history=InMemoryChatMessageHistory()

#


#Calling API Key
if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

#Header
st.markdown("<h1 style='text-align: center; color: White ;'>AI Chatbhatta 🌟</h1>", unsafe_allow_html=True)
st.markdown("This is a simple app that uses Google Gemini-2.5-Flash model to chat with AI.")
prompt= st.chat_input("Ask me anything....")

##Checking for Personal Information(If yes Warning to user, else fetches request.)
messages = [
    (
        "system",
        "You are a Personal Data Moderator. You analyse the user's data and then give a judgement if it contains any kind of personal information like name mobile number etc. You response should only be True or False, True if the data has PII else False"   
    ),
    ("human", f"{prompt}"),
    ]
ai_msg= llm.invoke(messages)

if prompt:
    if ai_msg.content=="True":
        st.warning("Warning: Do not share personal information online, including our Platform.")
    else:
        messages = [
    (
        "system",
        "You are a helpful AI assistant that answers the user question.",
    ),
    ("human", f"{prompt}"),
    ]
        ai_msg=llm.invoke(messages)
        reply=ai_msg.content
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            st.write((reply))
        print(messages)
        print(reply)


    
