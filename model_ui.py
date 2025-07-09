from dotenv import load_dotenv
import streamlit as st
import os
import speech_recognition as sr
from langchain import OpenAI
from audio_recorder_streamlit import audio_recorder
from streamlit_mic_recorder import speech_to_text

load_dotenv()
llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.8)


st.set_page_config(page_title="Ninja Bot")

st.header("Ninja Bot")

if'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]


input=st.text_input("Input:",key="input")


text = speech_to_text(
    language='en',
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    just_once=False,
    use_container_width=False,
    callback=None,
    args=(),
    kwargs={},
    key=None
)

res=""
out=0

if input:
    res=llm(input)
    st.session_state['chat_history'].append(("You",input))
    out=1
if text:
    res=llm(text)
    st.session_state['chat_history'].append(("You",text))
    out=1
if out==1:
    st.subheader("The response is")
    st.write(res)
    st.session_state['chat_history'].append(("Bot",res))
    out=0

st.subheader("The chat History")
for role,text in st.session_state['chat_history']:
    st.write(role,":",text)