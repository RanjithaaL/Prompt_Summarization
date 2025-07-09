import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import(
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.summarize import load_summarize_chain
import requests
from bs4 import BeautifulSoup

load_dotenv() #loads all environment variables
genai.configure(api_key=os.getenv('GOOGLE_API_KEY')) #to configure api key

llm=ChatGoogleGenerativeAI(model='gemini-pro',temperature=0.2,top_p=0.85)

print("Enter the topic")
topic=input()

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

