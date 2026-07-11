from dotenv import load_dotenv
import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

load_dotenv()
MODEL="llama-3.1-8b-instant"
prompt= ChatPromptTemplate.from_messages([
    ("system","You are a translater. Translate the text into {language}.Reply with only the translation."),
    ("human","{text}"),
])
print("Template variable needed", prompt.input_variables)
message=prompt.format_messages(language="French", text="Good morning!")
if not os.getenv("GROQ_API_KEY"):
    print("No API Key")
else:
    model=ChatGroq(model=MODEL)
    reply=model.invoke(message)
    print("Model Reply:", reply.content)