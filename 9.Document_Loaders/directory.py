from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

loader = DirectoryLoader(
    path="D:/Nitish_CampusX/Langchain/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()
#docs = loader.lazy_load()

print(len(docs))
print(docs[1].page_content)
print(docs[1].metadata)