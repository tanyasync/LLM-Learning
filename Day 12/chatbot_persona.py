import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
MODEL = "llama-3.1-8b- instant"
SYSTEM_PROMPT = (
    "You are sparky, a cheerful coding tutor for Indian B.Tech student who knows only basics"
    "Python, explain simply , use small examples and keep it under 3 sentences ")


def main() -> None:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    messages =[{"role":"system","content":SYSTEM_PROMPT}]
    print("sparky is ready. type /exit to quit.\n")
    
    while True:
        user_text = input ("You:   ").strip()
        
        if user_text.lower() in {"/exit","/quit"}:
            print("Bot : bye")
            break
        if not user_text:
            continue
        #1. Add user's message to the history
        messages.append({"role":"user","conetnt":user_text})
        chat = client.chat.completions.create(model=MODEL,messages=messages)
        reply = chat.choices[0].message.content.strip()
        #Add bot's reply too, so it remembers what it said
        messages.append({"role":"assistent","content":reply})
        print("Bot: ",reply,"\n")
        
if __name__=="__main__":
    main()