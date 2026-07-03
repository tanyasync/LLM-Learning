import os
import json
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
MODEL = "llama-3.1-8b-instant"
HISTORY_FILE = "chat_history.json"
SYSTEM_PROMPT = "you are a friendly, concise assistant. Keep replies short and clear"

def save(messages:list)->None:
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(messages,f,indent=2,ensure_ascii=False)
    print(f"Bot: Saved {len(messages)} messages to {HISTORY_FILE}.\n")
    
def load() -> list:
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            messages = json.load(f)
        print(f"Bot : Loaded {len(messages)} from {HISTORY_FILE}.\n")
        return messages
    except FileNotFoundError:
        print(f"Bot: No {HISTORY_FILE} yet -- nothing to load")
        return fresh_history()
        
def fresh_history() -> list:
    """A new conversatation: just the system messages"""
    return [{"role":"system", "content":SYSTEM_PROMPT}]

def main() -> None:
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    messages = fresh_history()
    print("chatbot Ready. Commands: /reset /history /save /load /exit \n")
    
    while True:
        user_text = input ("You:   ").strip()
        if not user_text:
            continue
        cmd = user_text.lower()
        if cmd in {"/exit","/quit"}:
            print("Bot: bye")
            break
        if cmd == "/reset":
            messages = fresh_history()
            print("Bot: conversation cleared.\n")
        if cmd == "/save":
            save (messages)
            continue
        if cmd == "/history":
            nos = sum(1 for m in messages if m ["role"] !="system")
            print(f"Bot: {nos} messages in history !")
            continue
        if cmd == "/load":
            messages = load()
            continue
        messages.append({"role":"user","content":user_text})
        chat = client.chat.completions.create(model=MODEL, messages=messages)
        reply= chat.choices[0].message.content.strip()
        messages.append({"role":"assistant","content":reply})
        print("bot:",reply, "\n")
        
        
if __name__ == "__main__":
    main()
    