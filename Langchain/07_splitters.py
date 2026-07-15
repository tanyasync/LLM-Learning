from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

POLICY = """
Refund policy. Customers may request a refund within 30 days of purchase.
Refunds are processed to the original payment method within 5 business days.
Shipping. We ship across India. Standard delivery takes 4 to 7 working days.
Express delivery (extra charge) arrives in 1 to 2 days in metro cities.

Support. Reach us at help@example.in or call 1800-123-456, 9am-6pm, Mon-Sat.
Our office is in Pune, Maharashtra.
""".strip()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=160,
    chunk_overlap=30,
    separators=["\n\n", "\n", ". ", " ", ""], 
)

chunks = splitter.split_text(POLICY)
print(f"Split {len(POLICY)} chars into {len(chunks)} chunks:\n")
for i, c in enumerate(chunks):
    print(f"--- chunk {i} ({len(c)} chars) ---")
    print(c)
    print()

docs = splitter.create_documents(
    [POLICY],
    metadatas=[{"source": "policy.txt"}],
)
print(f"As Documents: {len(docs)} of them. First one:")
first = docs[0]
print("  .page_content:", repr(first.page_content[:60]), "...")
print("  .metadata    :", first.metadata)    
print()

manual = Document(page_content="FAQ: yes, cash on delivery is available.",
                  metadata={"source": "faq", "topic": "payment"})
print("Hand-built Document:", manual.page_content, "|", manual.metadata)
print()

print("Takeaway: text -> Documents (content + metadata) -> chunks. That's RAG")
print("step 1. Next we embed these chunks and store them so we can search them.")
