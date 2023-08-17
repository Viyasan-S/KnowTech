import streamlit as st
import asyncio
import json
import re
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle

def ask(prompt):
    res = asyncio.run(ask_bot(prompt))
    return res

async def create_chatbot():
    cookies = json.loads(open("./cookies.json", encoding="utf-8").read())
    return await Chatbot.create(cookies=cookies)

async def ask_bot(prompt):
    bot = await create_chatbot()
    response = await bot.ask(prompt=prompt, conversation_style=ConversationStyle.creative, simplify_response=True)
    
    bot_response = response['text']
    
    await bot.close()
    
    return bot_response

st.title("Sample chat App")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = asyncio.run(ask_bot(prompt))
        
    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
    st.experimental_rerun()