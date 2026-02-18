from pymongo import MongoClient
from app.services.embedding import get_embedding_model
from app.services.document_loader import load_hr_documents  
from langchain_mongodb import MongoDBAtlasVectorSearch
from app.config import MONGODB_URI

def get_vector_store():
  

    client = MongoClient(MONGODB_URI)
    db = client["hr_ai_db"]
    collection = client["hr_ai_db"]["hr_policy_chunks"]
    embeddings = get_embedding_model()

    vector_store = MongoDBAtlasVectorSearch(
        collection=collection,
        embedding=embeddings,
        index_name="vector_index"  # <-- IMPORTANT
    )

    return vector_store