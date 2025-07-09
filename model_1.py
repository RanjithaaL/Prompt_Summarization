from dotenv import load_dotenv
import streamlit as st
import os
import speech_recognition as sr
from langchain import OpenAI

load_dotenv()
llm=OpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"),model_name="gpt-3.5-turbo-instruct",temperature=0.8)

def voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

def repeat_input(text):
    if text:
        print("Is: {} Correct??".format(text))
    else:
        print("No input received.")

def con():
        r = sr.Recognizer()
        with sr.Microphone() as so:
            print("Was it guessed right??\nCorrect or No")
            aud = r.listen(so)
        try:
            text1 = r.recognize_google(aud)
            text1=text1.lower()
            if text1=='correct':
                return 1
            elif text1=='no':
                return 0
            else:
                print("Sorry, I didn't understand your answer. Please answer with 'correct' or 'no'.")
                return con()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


def menu():
    print("Enter 1 for Text Input\n2 for Voice Input")
    a=int(input())
    return a

def text_input():
    print("Enter the text")
    a=input()
    print("The text was: ",a)
    res=llm(a)
    print(res)
    b=t_cont()
    if(b==1):
        text_input()

def v_input():
    while True:
        user_input = voice_input()
        #repeat_input(user_input)
        p=con()
        if(p==1):
            break
    res=llm(user_input)
    print(res)
    b=v_cont()
    if(b==1):
        v_input()

def t_cont():
    print("Do you want to continue??\nYes or No")
    a=input()
    a.lower()
    if(a=='yes'):
        return 1
    elif(a=='no'):
        return 2
    
def v_cont():
    r = sr.Recognizer()
    with sr.Microphone() as so:
        print("Do you want to continue??\nContinue or Stop")
        aud = r.listen(so)
        try:
            text1 = r.recognize_google(aud)
            text1=text1.lower()
            if text1=='continue':
                return 1
            elif text1=='stop':
                return 0
            else:
                print("Sorry, I didn't understand your answer. Please answer with 'continue' or 'stop'.")
                return con()
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


input_choice=menu()
if(input_choice==1):
    text_input()
elif(input_choice==2):
    v_input()
