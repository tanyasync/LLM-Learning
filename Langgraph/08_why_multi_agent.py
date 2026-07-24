"""The three shapes of an agent team (all just graphs):

1) SEQUENTIAL  (an assembly line)         -> Module 02
   START -> [research] -> [write] -> [edit] -> END
   Each agent adds one piece; state carries the hand-off forward.

2) SUPERVISOR / HIERARCHICAL (a boss)      -> Module 03
                 +-------------+
        +------> | supervisor  | <------+       the boss ROUTES work to a
        |        +------+------+        |       worker, the worker reports
        v               |              v        back, the boss decides who is
   [researcher]     [writer]       [editor]     next -- or that it's done.

3) PARALLEL  (fan-out / fan-in)            -> Module 04
                  +--> [fact-checker] --+
   [dispatch] ----+--> [seo-expert] ----+---> [merge]
                  +--> [tone-expert] ---+
   All specialists run at once; a reducer collects their notes.
"""

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