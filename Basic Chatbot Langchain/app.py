import streamlit as st
import time
from prompt import firePrompt

st.set_page_config(page_title='English LLM',
                   page_icon='👋',
                   layout='wide',
                   initial_sidebar_state='expanded'
                )

if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'temp' not in st.session_state:
    st.session_state.temp = 0

def getAvatar(role):
    if role == 'assistant':
        return 
    else :
        return 

def getContext():
    res = ""
    for item in st.session_state.messages[:-1]:
        res = res + f"role: {item['role']} content: {item['content']}\n"
    return res

st.markdown('# English AI Assistant 🤖', unsafe_allow_html=True)

with st.chat_message(name="assistant"):
    st.markdown('Hello Bot')
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=getAvatar(message["role"])):
        st.markdown(f'{message["content"]}')

if prompt := st.chat_input(placeholder="Chat with me. Let's chat in English!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user"):
        st.markdown(prompt)
    with st.chat_message(name='assistant'):
        message_placeholder = st.empty()
        full_response = ""
        with st.spinner(text="Thinking... 🤔"):            
            raw = firePrompt(st.session_state.messages[-1]['content'], temp=st.session_state.temp)
            response = str(raw)
            # Simulate stream of response with milliseconds delay
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
            message_placeholder.markdown(f'#### {full_response}', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_response})