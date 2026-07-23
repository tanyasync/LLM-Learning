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
def calculator(a:float,b:float,op:str)->float:
    """Do arithematic on two numbers.op is one of the add,sub,mul,div"""
    return{"add":a+b,"sub":a-b,"mul":a*b,"div":a/b  if b else float("nan")}[op]
@tool
def word_count(text:str)->int:
    """Count the numbers of words in a piece of text"""
    return len(text.split())
@tool
def lookup_note(topic: str) -> str:
    """Look up a short study note by topic. Topics: python, groq, rag, agent."""
    notes = {
        "python": "Python is a high-level language; indentation defines blocks.",
        "groq": "Groq serves open models fast and has a genuinely free tier.",
        "rag": "RAG = retrieve relevant text, then answer grounded in it.",
        "agent": "An agent loops: reason, call a tool, observe, repeat.",
    }
    return notes.get(topic.lower(), f"No note found for '{topic}'.")


TOOLS = [calculator, word_count, lookup_note]

SYSTEM_PROMPT = (
    "You are StudyBot, a concise study assistant for engineering students. "
    "Always use a tool for arithmetic, counting, or looking up a note -- never "
    "guess. After using tools, answer in one short, friendly sentence."
)
if os.getenv("GROQ_API_KEY"):
    from langchain_groq import ChatGroq
    model=ChatGroq(model=MODEL, temperature=0)
    agent=create_agent(model,TOOLS,system_prompt=SYSTEM_PROMPT)
    question="Give me the note on 'agent' and also what is 3 times 4"
    result=agent.invoke({"messages":[("human",question)]})
    print(result['messages'])
else:
    print("NO_KEY_FOUND")