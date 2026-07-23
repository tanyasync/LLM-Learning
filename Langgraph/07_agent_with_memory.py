import os 
from typing import List
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langgraph.checkpoint.memory import MemorySaver
load_dotenv()
MODEL="llama-3.1-8b-instant"
@tool
def add(a:int,b:int)->int:
    """Add two integers a and b and return the sum"""
    return a+b
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model=ChatGroq(model=MODEL,temperature=0)
    agent=create_agent(model,[add],checkpointer=MemorySaver())
    config={"configurable":{"thread_id":"student-1"}}
    response1=agent.invoke({"messages":[("human","HI, My name is Tanya, I am 21 years old, I live in lucknow")]},config)
    print(response1['messages'][-1].content)
    response2=agent.invoke({"messages":[("human","what is my name?")]},config)
    print(response2['messages'][-1].content)
    response3=agent.invoke({"messages":[("human","How old am i?")]},config)
    print(response3['messages'][-1].content)
    response4=agent.invoke({"messages":[("human","where do i live?")]},config)
    print(response4['messages'][-1].content)
else:
    print("NO_API_KEY")