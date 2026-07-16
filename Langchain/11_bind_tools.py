import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool

load_dotenv()

MODEL = "llama-3.1-8b-instant"

@tool
def multiply(a: int, b: int) -> int:
    """multiply two int and return the exact result"""
    return a * b

@tool
def word_count(text: str) -> int:
    """count how many words are there in a text"""
    return len(text.split())

TOOLS = [multiply, word_count]

questions = [
    "what is 24*7",
    "how many words in 'How is the weather today?'",
    "say hello in one word."
]

from langchain_groq import ChatGroq

llm = ChatGroq(model=MODEL, temperature=0)
llm_with_tools = llm.bind_tools(TOOLS)

for q in questions:
    print("=" * 60)
    print(f"Q: {q}")

    try:
        resp = llm_with_tools.invoke(q)

        if resp.tool_calls:
            for call in resp.tool_calls:
                print(f"Model wants tool: {call['name']} args={call['args']}")
                print("(content is empty - model waiting for tool)")
        else:
            print(f"No tools needed. answer: {resp.content}")

    except Exception as e:
        print(f"Error: {e}")