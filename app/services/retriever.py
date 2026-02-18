from app.services.vector_store import get_vector_store
vector_store = get_vector_store()

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 3
    }
)