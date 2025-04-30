from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional
import os

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")

model = ChatOpenAI(model="gpt-4", api_key=API_KEY_OPENAI)

# schema 

class Review(TypedDict):
    key_themes: Annotated[list[str],"Write down all the key themes discussed in the review"]
    summary : Annotated[str,"A brief summary of the review"]
    sentiment: Annotated[str,"Return the sentiment of the review either negative or positive or neutral"]
    prose: Annotated[Optional[list[str]],"Write down all the pros inside the list"]
    con: Annotated[Optional[list[str]],"Write down all the cons inside the list"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.
The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.
However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.
""")

print(result)