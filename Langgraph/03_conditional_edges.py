from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    message: str      # the incoming support message
    category: str     # set by classify()
    reply: str        # set by one of the handler nodes
    
def classify(state:State)->dict:
    text = state["message"].lower()
    if any(w in text for w in ("refund", "charge", "invoice", "payment")):
        category = "billing"
    elif any(w in text for w in ("error", "crash", "bug", "login", "broken")):
        category = "technical"
def route(state: State) -> str:
    return state["category"] 

def billing(state: State) -> dict:
    return {"reply": "Billing team here -- we'll review your charge within 24h."}

def technical(state: State) -> dict:
    return {"reply": "Tech support here -- please share your app version & a screenshot."}

def general(state: State) -> dict:
    return {"reply": "Thanks for reaching out! A team member will get back to you."}
