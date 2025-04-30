from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",api_key=API_KEY_OPENAI)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Tell me about Socialism")
]

result = model.invoke(messages)

messages.append(AIMessage(content = result.content))

print(messages)