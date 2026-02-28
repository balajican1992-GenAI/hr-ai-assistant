from app.services.vector_store import get_vector_store
from app.services.rag_service import get_rag_chain

if __name__ == "__main__":
    rag = get_rag_chain()
    vector_store = get_vector_store()
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 6, "fetch_k": 20}
    )
    docs = retriever.invoke("What is leave policy?")
    print("Docs count:", len(docs))

    for doc in docs:
        print(doc.page_content)
   
    #print(response)