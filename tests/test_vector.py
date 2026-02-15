from app.services.document_loader import load_hr_documents
from app.services.text_splitter import split_documents
from app.services.embedding import get_embedding_model
from app.services.vector_store import get_vector_store

def test_embedding_and_vectorstore():
    print("Loading documents...")
    docs = load_hr_documents()
    print(f"Total documents loaded: {len(docs)}")

    print("Splitting documents into chunks...")
    chunks = split_documents(docs)
    print(f"Total chunks created: {len(chunks)}")

    print("Creating embedding model...")
    embeddings = get_embedding_model()
    print("Embedding model loaded ✅")

    print("Connecting to MongoDB vector store...")
    vector_store = get_vector_store()
    print("Vector store connected ✅")

    print("Storing chunks into vector store...")
    try:
        vector_store.add_documents(chunks)
        print("Chunks stored successfully ✅")
    except Exception as e:
        print("Error storing chunks:", e)

    print("Testing retrieval from vector store...")
    try:
        retriever = vector_store.as_retriever(search_kwargs={"k": 2})
        results = retriever.invoke("What is the maternity leave policy?")
        for i, res in enumerate(results):
            print(f"Result {i+1}: {res.page_content[:200]}...")  # preview
        print("Retrieval test passed ✅")
    except Exception as e:
        print("Error retrieving from vector store:", e)

if __name__ == "__main__":
    test_embedding_and_vectorstore()