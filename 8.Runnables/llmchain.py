from langchain.llms import OpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()


#API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

llm = OpenAI(model_name="gpt-4o", temperature=0.7)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="suggest a catchy blog title about {topic}"
)

chain = LLMChain(llm=llm,prompt=prompt)

topic=input("Enter a topic: ")
output = chain.run(topic)

print("Generated Blog Title", output)