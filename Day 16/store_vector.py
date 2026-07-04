# `Path` helps us build reliable folder paths relative to this file.
from pathlib import Path

# Chroma is the local vector database we use to save and retrieve vectors.
import chromadb
# SentenceTransformer gives us a local embedding model: text -> vector.
from sentence_transformers import SentenceTransformer


# `BASE_DIR` points to the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent
# `DB_DIR` is where Chroma will save its database files on disk.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` is the logical table-like name inside Chroma.
COLLECTION_NAME = "student_notes"

# These are the notes we want to embed and store.
NOTES = [
    {
        "id": "note-1",
        "topic": "algorithms",
        "document": "Binary search only works on sorted data. Check the middle and discard half each step.",
    },
    {
        "id": "note-2",
        "topic": "python",
        "document": "Use a dictionary when you need fast key lookup instead of scanning a full list.",
    },
    {
        "id": "note-3",
        "topic": "prompting",
        "document": "Good prompts include the role, task, constraints, and the output format you want.",
    },
    {
        "id": "note-4",
        "topic": "recursion",
        "document": "Recursion needs a base case and a smaller subproblem so the calls eventually stop.",
    },
]


def main() -> None:
    # Load the local embedding model used throughout this day.
    model = SentenceTransformer("all-MiniLM-L6-v2")
    # Pull out only the raw note text because that is what we embed.
    documents = [note["document"] for note in NOTES]
    # Convert every note into a vector, then convert numpy arrays to plain Python lists for Chroma.
    embeddings = model.encode(documents).tolist()

    # Open a persistent Chroma client so data is saved inside `DB_DIR`.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Create the collection if it does not exist, or reuse it if it already exists.
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        # Tell Chroma to treat distance as cosine distance for vector search.
        metadata={"hnsw:space": "cosine"},
    )

    # Upsert means "insert new rows or overwrite existing rows with the same ids".
    collection.upsert(
        # Stable ids let us update the same note later if needed.
        ids=[note["id"] for note in NOTES],
        # These are the actual text documents we want to retrieve later.
        documents=documents,
        # Metadata travels with each vector so we can display or filter by topic later.
        metadatas=[{"topic": note["topic"]} for note in NOTES],
        # These are the embedding vectors for each document.
        embeddings=embeddings,
    )

    # Print a small status summary so students can see what got stored.
    print("=" * 72)
    print("Saved note vectors to Chroma")
    print("=" * 72)
    print(f"Database folder : {DB_DIR}")
    print(f"Collection name : {COLLECTION_NAME}")
    print(f"Stored records  : {collection.count()}")

    # Print every stored note so students can match ids/topics to documents.
    print("\nStored notes:")
    for note in NOTES:
        print(f"- {note['id']} [{note['topic']}] {note['document']}")


# Run `main()` only when this file is executed directly.
if __name__ == "__main__":
    main()