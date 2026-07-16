from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """multiply two int and return the exact result"""
    return a * b

@tool
def word_count(text: str) -> int:
    """count how many words are there in a text"""
    return len(text.split())

print("=" * 60)
print("what the model sees about each tool")
print("=" * 60)

for t in (multiply, word_count):
    print(f"name :{t.name}")
    print(f"description :{t.description}")
    print(f"args :{t.args}")
    print("=" * 60)

print(multiply.invoke({"a": 56, "b": 45}))
print(word_count.invoke({"text": "tools let model act"}))