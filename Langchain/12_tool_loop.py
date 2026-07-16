import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage , AImessage, ToolMessage
load_dotenv()
MODEL="llama-3.1-8b-instant"\
@tool
def multiply(a: int, b: int) -> int:
    """multiply two int and return the exact result"""
    return a * b

@tool
def word_count(text: str) -> int:
    """count how many words are there in a text"""
    return len(text.split())