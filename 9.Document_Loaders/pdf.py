from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",api_key=API_KEY_OPENAI)
loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

print(len(docs))

print(docs[1].metadata)