from typing import TypedDict
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
load_dotenv()
llm=ChatGroq(model="llama-3.1-8b-instant",temperature=0)
class State(TypedDict):
    topic:str
    research:str
    draft:str
    final:str
def _ask(role_system: str, user: str) -> str:
    reply = llm.invoke([SystemMessage(content=role_system), HumanMessage(content=user)])
    return reply.content.strip()

def researcher(state: State) -> dict:
    """Agent 1: gather a few crisp facts about the topic."""
    system = (
        "You are a Researcher. Given a topic, list 3 short factual bullet points "
        "a writer could use. Bullets only, no intro."
    )
    research = _ask(system, f"Topic: {state['topic']}")
    print("\n[researcher] produced notes:\n" + research)
    return {"research": research}

def writer(state: State) -> dict:
    """Agent 2: turn the researcher's notes into a short paragraph."""
    system = (
        "You are a Writer. Using ONLY the research notes provided, write one "
        "engaging paragraph (3-4 sentences) for a general audience."
    )
    draft = _ask(system, f"Topic: {state['topic']}\n\nResearch notes:\n{state['research']}")
    print("\n[writer] produced a draft:\n" + draft)
    return {"draft": draft}