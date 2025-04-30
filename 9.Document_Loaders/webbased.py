from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
import os
load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",api_key=API_KEY_OPENAI)

prompt = PromptTemplate(
    template="Answer the following question \n {question} from the following text \n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421'
loader = WebBaseLoader(url)

pages = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question':'What is the peak brightness of this product','text':pages[0].page_content}))