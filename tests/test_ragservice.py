from app.services.vector_store import get_vector_store
from app.services.rag_service import get_rag_chain
from app.config import MONGODB_URI
from pymongo import MongoClient

if __name__ == "__main__":
    rag = get_rag_chain()
    vector_store = get_vector_store()
    client = MongoClient(MONGODB_URI)
    collection = client["hr_ai_db"]["hr_policy_chunks"]

    #collection = vector_store._collection.database[vector_store._collection.name]

    print("Document count:", collection.count_documents({}))
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 6, "fetch_k": 20}
    )
    docs = retriever.invoke("What is leave policy?")
    print("Docs count:", len(docs))

    for doc in docs:
        print(doc.page_content)
   
    #print(response)