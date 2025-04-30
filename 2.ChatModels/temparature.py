from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",temperature=1.5,api_key=API_KEY_OPENAI)

response = model.invoke("write a five line poem on Cricket.")

print(response.content)

