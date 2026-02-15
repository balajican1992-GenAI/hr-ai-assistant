from pymongo import MongoClient
from app.services.embedding import get_embedding_model
from langchain_mongodb import MongoDBAtlasVectorSearch
from app.config import MONGODB_URI

def get_vector_store():
    client = MongoClient(MONGODB_URI)
    db = client["hr_ai_db"]
    collection = db["hr_policy_chunks"]

    embeddings = get_embedding_model()

    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name="vector_index"
    )

    return vector_store