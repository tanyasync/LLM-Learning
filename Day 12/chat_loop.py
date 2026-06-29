import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()
MODEL = "llama-3.1-8b-instant"

def ask(client:Groq, user_text:str) -> str:
    #send a sinle message and return the reply text
    chat = client.chat.completions.create(
        model= MODEL,
        messages =[
            {
                "role":"user",
                "content":user_text
            }
        ]
    )
    return chat.choices[0].message.content.strip()
def main() -> None:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    print("Chatbot Ready. Type /exit to quit.\n")
    
    while True:
        user_text = input("You: ").strip()
        if user_text.lower() in {"/exit","/quit"}:
            print("Bot: Bye")
            break
        if not user_text:
            continue
        reply = ask(client,user_text)
        print("Bot:",reply,"\n")
        
if __name__=="__main__":
    main()