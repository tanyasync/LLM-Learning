# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage, AIMessage
# load_dotenv()

# llm = ChatGroq(
#     model="llama-3.1-8b-instant",
#     temperature=0.7
# )
# chat_history = []
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Bot: Goodbye!")
#         break
    
#     chat_history.append(
#         HumanMessage(content=user_input))
#     response = llm.invoke(chat_history)
    
#     chat_history.append(
#     AIMessage(content=response.content))
#     print("Bot:", response.content)
    
    
from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
load_dotenv()

MODEL = "llama-3.1-8b-instant"

llm = ChatGroq(
    model=MODEL,
    temperature=0
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly AI assistant. Answer briefly and helpfully."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | llm | StrOutputParser()
history = []

print("=" * 50)
print(" CLI Chatbot Started")
print("Type 'exit' or 'quit' to stop.")
print("=" * 50)

while True:
    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        print("\nBot: Goodbye! 👋")
        break

    response = chain.invoke({
        "history": history,
        "input": user_input
    })

    print(f"Bot: {response}")

    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))

    print("\n----- Current History -----")
    for message in history:
        if isinstance(message, HumanMessage):
            print(f"You: {message.content}")
        else:
            print(f"Bot: {message.content}")
    print("-" * 30)

print("\n========== Final Conversation History ==========\n")

for message in history:
    if isinstance(message, HumanMessage):
        print(f"You: {message.content}")
    else:
        print(f"Bot: {message.content}")