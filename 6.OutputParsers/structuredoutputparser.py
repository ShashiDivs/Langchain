from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()



GROQ_API_KEY = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="qwen-qwq-32b",api_key=GROQ_API_KEY)

schema = [
    ResponseSchema(name="fact_1",description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2",description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3",description="Fact 3 about the topic"),

]

parser =  StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 Facts about {topic} \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)

prompt = template.invoke({"topic":"black hole"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)