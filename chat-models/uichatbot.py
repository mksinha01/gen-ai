import streamlit as st

from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI

# Initialize messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="you are chef")
    ]

# Model
model = ChatOpenAI(model="gpt-4.1", temperature=0.5, max_tokens=200)

st.title("AI Chatbot")
st.write("Type 0 to exit")

# Input box
prompt = st.text_input("Chat now")

if prompt:
    if prompt == "0":
        st.stop()

    st.session_state.messages.append(HumanMessage(content=prompt))

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    st.write("bot :", response.content)