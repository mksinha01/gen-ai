from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

from huggingface_hub import InferenceClient

client = InferenceClient()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    model="deepseek-ai/DeepSeek-R1",
    client=client,
    async_client=None
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("write a poem on a man!")
print(response.content)
