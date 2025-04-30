from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()



GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="qwen-qwq-32b",api_key=GROQ_API_KEY)


template1 = PromptTemplate(
    template = "write a detailed report on {topic}",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template = "write a 5 line summary on the following text. /n {text}",
    input_variables=["text"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)