from typing import TypedDict, Annotated
from operator import add
from langgraph.graph import StateGraph, START, END, MessagesState
from langgraph.graph.message import add_messages

class NoReducer(TypedDict):
    log:list
def step_a(state):return {"log":["a ran"]}
def step_b(state):return {"log":["b ran"]}

b1=StateGraph(NoReducer)
b1.add_node("step_a", step_a)
b1.add_node("step_b", step_b)
b1.add_edge(START, "step_a")
b1.add_edge("step_a","step_b")
b1.add_edge("step_b",END)
print(b1.compile().invoke({"log":[]}))

class WithReducer(TypedDict):
    log:Annotated[list,add]
    
b2=StateGraph(NoReducer)
b2.add_node("step_a", step_a)
b2.add_node("step_b", step_b)
b2.add_edge(START, "step_a")
b2.add_edge("step_a","step_b")
b2.add_edge("step_b",END)
print(b2.compile().invoke({"log":[]}))
