from dotenv import load_dotenv
import os

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

# 1. Load your .env and read the correct key
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

# 2. Instantiate the chat model correctly
model = ChatOpenAI(
    model_name="gpt-4",
    openai_api_key=openai_api_key
)

# 3. Load and split your document
loader = TextLoader("cricket.txt", encoding="utf-8")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

# 4. Create embeddings and FAISS vector store
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
vectorstore = FAISS.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever()

# 5. Build the RetrievalQA chain
chain = RetrievalQA.from_chain_type(
    llm=model,
    chain_type="stuff",
    retriever=retriever
)

# 6. Run your query (fixed typo)
query = "What are the key takeaways from the document?"
answer = chain.run(query)
print(answer)
