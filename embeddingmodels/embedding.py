from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()


embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimensions=64
)
text = [
    "Hello world",
    "Bye bye",
    "hello AI"
                ]
response = embeddings.embed_documents(text)
print(response)
# vector= embeddings.embed_query("Hello world")
# print(vector)