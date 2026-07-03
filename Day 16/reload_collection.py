"""
Day 18 - Step 2: Reload the saved Chroma collection in a fresh script.
"""

# `Path` lets us point back to the same database folder used in step 1.
from pathlib import Path

# Chroma is the database we are reconnecting to.
import chromadb


# `BASE_DIR` is the Day 18 folder.
BASE_DIR = Path(__file__).resolve().parent.parent
# `DB_DIR` must match step 1, otherwise we would open a different database.
DB_DIR = BASE_DIR / "chroma_store"
# `COLLECTION_NAME` must also match the collection created earlier.
COLLECTION_NAME = "student_notes"


def main() -> None:
    # Open the saved Chroma database from disk.
    client = chromadb.PersistentClient(path=str(DB_DIR))
    # Reconnect to the existing collection by name.
    collection = client.get_collection(COLLECTION_NAME)
    # Fetch stored ids, documents, and metadata so we can inspect what survived.
    snapshot = collection.get(include=["documents", "metadatas"])

    # Print a small summary showing that the database reopened successfully.
    print("=" * 72)
    print("Reloaded Chroma collection from disk")
    print("=" * 72)
    print(f"Database folder : {DB_DIR}")
    print(f"Collection name : {COLLECTION_NAME}")
    print(f"Stored records  : {collection.count()}")

    # Print each saved record to prove the vectors/documents persisted across runs.
    print("\nSnapshot:")
    for doc_id, metadata, document in zip(
        snapshot["ids"],
        snapshot["metadatas"],
        snapshot["documents"],
    ):
        # Use a fallback topic just in case metadata is missing.
        topic = metadata.get("topic", "unknown")
        print(f"- {doc_id} [{topic}] {document}")


# Run this script only when executed directly.
if __name__ == "__main__":
    main()