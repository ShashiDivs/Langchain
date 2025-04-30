from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",api_key=API_KEY_OPENAI)


chat_template = ChatPromptTemplate([
    ("system","You are a helpful {domain} expert"),
    ("human","Explain in simple terms, what is {topic}")
    # SystemMessage(content="You are a helpful {domain} expert"),
    # HumanMessage(content="Explain in simple terms, what is {topic}")
])

prompt = chat_template.invoke({"domain":"philosophy","topic":"Epistemology"})

print(prompt)