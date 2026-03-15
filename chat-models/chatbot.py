from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

# model = init_chat_model("gpt-4.1")
# response = model.invoke("what is youer ip address?")
# print(response.content)
messages =[]
from langchain_openai import ChatOpenAI
model = ChatOpenAI(model="gpt-4.1",temperature=0.5,max_tokens=20)
print("______________________________welcome type 0 to exit ______________________________")
while True :

    promt = input("chat now : ")
    messages.append(promt)
    if promt== "0":
        break
    response = model.invoke(messages)
    messages.append(response.content)
    print("bot : ",response.content)