
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")
# response = model.invoke("what is youer ip address?")
# print(response.content)

from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4.1",temperature=0.5,max_tokens=20)
response = model.invoke("write a poem on a man!")
print(response.content)