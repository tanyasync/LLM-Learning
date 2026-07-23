import os 
from typing import List
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_core.messages import AIMessage
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.outputs import ChatResult,ChatGeneration
load_dotenv()
MODEL="llama-3.1-8b-instant"
@tool
def multiply(a:int,b:int)->int:
    """Multiply two integers a and b and return the product"""
    return a*b
def add(a:int,b:int)-> int:
    """Add two integers a and b and return the sum"""
    return a+b
TOOLS=[add,multiply]
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model=ChatGroq(model=MODEL,temperature=0)
    agent=create_agent(model,TOOLS)
    question="What is 12 times 9"
    # result=agent.invoke({"messages":[("human",question)]})
    for chunk in agent.stream({"messages":[("human",question)]},stream_node="updates"):
        for node,updates in chunk.items():
            last = updates["messages"][-1]
            if getattr(last,"tool_calls",None):
                c=last.tool_calls[0]
                print(f"[{node}] REASON+ACT-> call{c['name']}(c['args])")
            elif type(last).__name__ =="ToolMessage":
                print(f"Observer->tool returned {last.content}")
            elif last.content:
                print(f"[{node:5}] ANSWER ->{last.content!r}")
else:
    print("NO_API_KEY")