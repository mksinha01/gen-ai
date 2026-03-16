from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
# langchain meassages core 
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage 
# model = init_chat_model("gpt-4.1")
# response = model.invoke("what is youer ip address?")
# print(response.content)
messages =[
    SystemMessage(content="you are chef")
]
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4.1",temperature=0.5,max_tokens=20)
print("______________________________welcome type 0 to exit ______________________________")
while True :

    promt = input("chat now : ")
    messages.append(HumanMessage(content=promt))
    if promt== "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("bot : ",response.content)