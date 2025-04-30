from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_core.output_parsers import StrOutputParser
load_dotenv()



API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4",api_key=API_KEY_OPENAI)

prompt = PromptTemplate(
    template="Generate 5 interest facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | StrOutputParser()

response = chain.invoke({'topic':'philosophy'})

#print(response)

chain.get_graph().print_ascii()
