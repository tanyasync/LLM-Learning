import os
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()
MODEL="llama-3.1-8b-instant"
st.set_page_config(page_title="LangchainChatbot",page_icon="💬")
st.title("Langchain + Chatbot")
if not os.getenv("GROQ_API_KEY"):
    st.info("No API key")
    st.stop()

@st.cache_resource
def get_chain():
    from langchain_groq import ChatGroq
    prompt=ChatPromptTemplate.from_messages([
        ("system","You are a helpful assistant"),
        MessagesPlaceholder("history"),
        ("human","{input}")
    ])
    model=ChatGroq(model=MODEL,temperature=0.3)
    return prompt | model | StrOutputParser()

chain=get_chain()

if "messages" not in st.session_state:
    st.session_state.messages=[]
    
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])
        
if user_text:= st.chat_input("Ask me anything"):
    st.session_state.messages.append({"role":"user", "content":user_text})
    with st.chat_message("user"):
        st.markdown(user_text)
        
    history=[]
    for m in st.session_state.messages[:-1]:
        cls=HumanMessage if m["role"] == "user" else AIMessage
        history.append(cls(content=m["content"]))
        
    with st.chat_message("assistant"):
        reply = st.write_stream(chain.stream({"history": history, "input": user_text}))

    # Store the assistant reply so it's there on the next rerun.
    st.session_state.messages.append({"role": "assistant", "content": reply})
    
with st.sidebar:
    st.header("Chat")
    st.caption(f"{len(st.session_state.messages)} messages so far.")
    if st.button("Clear conversation"):
        st.session_state.messages = []
        st.rerun()