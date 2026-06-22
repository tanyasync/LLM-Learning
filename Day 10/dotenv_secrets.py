import os
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()
demo_key = os.environ.get("DEMO_API_KEY")
if(demo_key):
    print("Found", demo_key)
else:
    print("Not found")