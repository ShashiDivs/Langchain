from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_OPENAI = os.getenv("API_KEY_OPENAI")


from openai import OpenAI

client = OpenAI(api_key=API_KEY_OPENAI)

response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)
