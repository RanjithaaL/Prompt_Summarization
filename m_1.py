import speech_recognition as sr
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chains.summarize import load_summarize_chain
import requests
from bs4 import BeautifulSoup

genai.configure(api_key='AIzaSyD1lSixXAqeC9NYs2tCjirVBgWYKsGE4fs')

llm=ChatGoogleGenerativeAI(model='gemini-pro',temperature=0.2,top_p=0.85)


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
            print("Was it guessed right??\nContinue or No")
            aud = r.listen(so)
        try:
            text1 = r.recognize_google(aud)
            text1=text1.lower()
            if text1=='continue':
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
    print("Enter the topic")
    a=input()
    print("The topic was: ",a)
    summary(a)
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
    summary(user_input)
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
        


def summary(topic):

    a="https://en.wikipedia.org/wiki/"+topic
    req=requests.get(a)
    soup= BeautifulSoup(req.content, "html.parser")
    text=soup.get_text()


    template=''' write a consice and short summary of the following document .
    text:'{text}' '''

    prompt1=PromptTemplate(
        input_variables=['text'],
        template=template
    )

    text_split=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=20)
    chunks=text_split.create_documents({text})

    chain=load_summarize_chain(
        llm,
        chain_type='map_reduce',
        verbose=False

    )
    summary=chain.invoke(chunks)
    print(summary)

    chunk_prompt=''' 
    summerise the below document:
    documment:'{text}'
    summary:
    '''
    map_reduce_temp=PromptTemplate(input_variables=['text'],
                                template=chunk_prompt)

    final_prompt='''  provide a final summary of the entire document with important points.
    add a generic title and start the summary with an introduction.
    provide the summary in points
    document:'{text}'
    '''

    final_template=PromptTemplate(input_variables=['text'],
                                template=final_prompt)

    summary_final=load_summarize_chain(
        llm=llm,
        chain_type='map_reduce',
        map_prompt=map_reduce_temp,
        combine_prompt=final_template,
        verbose=False 

    )
    output=summary_final.invoke(chunks)

    print(output)
    
    

input_choice=menu()
if(input_choice==1):
    text_input()
elif(input_choice==2):
    v_input()


