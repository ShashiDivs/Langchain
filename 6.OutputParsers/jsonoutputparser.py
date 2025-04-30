from langchain_core.output_parsers import JsonOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()


json_parser = JsonOutputParser()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="qwen-qwq-32b",api_key=GROQ_API_KEY)

template = PromptTemplate(
    template="Give me the name, age and city of the fictional person \n {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction":json_parser.get_format_instructions()}
)

prompt = template.format()

result = model.invoke(prompt)

final_result = json_parser.parse(result.content)

print(final_result)