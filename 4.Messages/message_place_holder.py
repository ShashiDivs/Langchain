from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain.schema import AIMessage, HumanMessage, SystemMessage

# Load environment variables
load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

# Initialize model
model = ChatOpenAI(model="gpt-4", api_key=API_KEY_OPENAI)

# Define chat template properly
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# Load chat history properly
chat_history = []
with open('data/chat_history.txt') as f:
    for line in f:
        chat_history.append(AIMessage(content=line.strip()))  # Assuming chat history contains AI messages

# Format the prompt correctly
prompt = chat_template.format(chat_history=chat_history, query="Where is my refund?")

# Invoke the model
response = model.invoke(prompt)

print(response.content)
