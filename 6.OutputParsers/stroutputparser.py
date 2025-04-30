from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="qwen-qwq-32b",api_key=GROQ_API_KEY)


template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "write a pipeline summary on the following text. /n {text}",
    input_variables=["text"]
)

prompt1 = template1.invoke({'topic':'black hole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)

print(result1.content)