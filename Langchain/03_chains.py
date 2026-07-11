"""
chain pieces with
chain = prompt | model | parser

"""

from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq

load_dotenv()
MODEL="llama-3.1-8b-instant"

to_upper=RunnableLambda(lambda s: s.upper())
add_bang=RunnableLambda(lambda s:s + "!")
tiny_chain=to_upper | add_bang
print(tiny_chain.invoke("hello"))
prompt=ChatPromptTemplate.from_messages([
    ("system","you are a helpful assistant.Answer in one short sentence"),
    ("human","{question}")
])
parser=StrOutputParser()
if not os.getenv("GROQ_API_KEY"):
    print("No GROQ Key")
else:
    model=ChatGroq(model=MODEL)
    chain=prompt | model | parser
    answer=chain.invoke({"question": "what is python"})
    print(answer)
    answer2=chain.stream({"question":"what are 3 newton's law of motion"})
    for piece in answer2:
        print(piece,end="",flush=True)
    
    questions=[
        {"question": "what is HTML?"},
        {"question":"what is HTTP?"},
    ]
    
    # answer3=chain.batch(questions)
    # print(answer3)
    for q,a in zip(questions,chain.batch(questions)):
        print(f"batch-> {q['question']}{a}")
        print()