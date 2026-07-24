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

def editor(state: State) -> dict:
    """Agent 3: tighten the writer's draft into a final version."""
    system = (
        "You are an Editor. Improve clarity and flow of the draft. Fix any awkward "
        "wording. Return ONLY the polished paragraph."
    )
    final = _ask(system, state["draft"])
    print("\n[editor] produced the final:\n" + final)
    return {"final": final}

def build_pipeline():
    g = StateGraph(State)
    g.add_node("researcher", researcher)
    g.add_node("writer", writer)
    g.add_node("editor", editor)
    g.add_edge(START, "researcher")     
    g.add_edge("researcher", "writer")  
    g.add_edge("writer", "editor")      
    g.add_edge("editor", END)           
    return g.compile()

def main() -> None:
    pipeline=build_pipeline()
    topic="why python is popular in AI"
    result = pipeline.invoke({"topic": topic, "research": "", "draft": "", "final": ""})
    
    print("\n" + "=" * 70)
    print("FINAL OUTPUT")
    print("=" * 70)
    print(result["final"])
    
    print(
        "\nWhat happened: the state carried the hand-off. The writer never saw the\n"
        "topic 'raw' -- it saw the researcher's notes. Each agent trusted the\n"
        "previous one's output. That's an assembly line."
    )
if __name__ == "__main__":
    main()
