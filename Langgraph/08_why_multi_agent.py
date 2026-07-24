from typing import TypedDict
from langgraph.graph import StateGraph, START,END

class State(TypedDict):
    topic:str
    draft:str
    log:list
def writer(state:State)->dict:
    draft=f"{state['topic']} is useful because it saves time."
    return {"draft":draft,"log":["write wrote a rough draft"]}
def editor(state:State)->dict:
    polished = state["draft"].replace("useful","genuinely useful").rstrip(".")+"!"
    return{"draft":polished,"log": state["log"]+["Editor polished the draft"]}

def build_team():
    g = StateGraph(State)
    g.add_node("writer", writer)
    g.add_node("editor", editor)
    g.add_edge(START, "writer")   # start hands the topic to the writer
    g.add_edge("writer", "editor")  # writer hands the draft to the editor
    g.add_edge("editor", END)
    return g.compile()

def main()->None:
    team=build_team()
    result=team.invoke({"topic":"LangGraph","draft":"","log":[]})
    print("\nFinal Draft:",result["draft"])
if __name__=="__main__":
    main()