from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text:str
#A node - simple function that takes current state and returns dict of keys to update
def shout(state:State)->dict:
    return {"text":state["text"].upper()+"!"}
builder=StateGraph(State)
builder.add_node("shout",shout)
# Edges say "what runs next". START is the entry point, END is the exit.
builder.add_edge(START,"shout") # begin -> shout
builder.add_edge("shout",END)   # shout -> done
graph = builder.compile()
result=graph.invoke({"text":"hello Laanggraph"})
print(result)
