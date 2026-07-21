from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    raw:str          # the original input
    cleaned:str      # filled by clean()
    word_count:int   # filled by count_words()
    shape:str        # filled by summarize_shape()

def clean(state:State)-> dict:
    text=state["raw"].strip().replace("  "," ")
    return {"cleaned":text}
def count_words(state:State)-> dict:
    n = len(state["cleaned"].split())
    return {"word_count":n}
def summarize_shape(state:State)->dict:
    n=state["word_count"]
    shape="short" if n<5 else "medium" if n<12 else "long"
    return {"shape":shape}

builder=StateGraph(State)
builder.add_node("clean",clean)
builder.add_node("count_words",count_words)
builder.add_node("summarize_shape", summarize_shape)

builder.add_edge(START, "clean")
builder.add_edge("clean","count_words")
builder.add_edge("count_words", "summarize_shape")
builder.add_edge("summarize_shape", END)
graph = builder.compile()
start = {"raw": "  LangGraph  passes state  from node  to node  "}
final = graph.invoke(start)
print()
print("Final state (every node's work is here):")
for key, value in final.items():
    print(f"  {key:12} = {value!r}")

print()
print("Takeaway: nodes are functions; each returns just what it changed; the")
print("shared state carries every node's result forward. That's the whole model.")