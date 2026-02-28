from pathlib import Path
from app.services.embedding import get_embedding_model
from app.services.document_loader import load_hr_documents
from app.services.text_splitter import split_documents
from langchain_community.vectorstores import FAISS

BASE_DIR = Path(__file__).resolve().parents[2]
FAISS_INDEX_DIR = BASE_DIR / "data" / "faiss_index"


def _build_faiss_index(index_dir: Path):
    docs = load_hr_documents()
    chunks = split_documents(docs)

    if not chunks:
        raise ValueError("No document chunks found to build FAISS index")

    embeddings = get_embedding_model()
    vector_store = FAISS.from_documents(chunks, embeddings)

    index_dir.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(index_dir))
    return vector_store


def get_vector_store(rebuild: bool = False):
    embeddings = get_embedding_model()
    index_file = FAISS_INDEX_DIR / "index.faiss"

    if rebuild or not index_file.exists():
        return _build_faiss_index(FAISS_INDEX_DIR)

    return FAISS.load_local(
        str(FAISS_INDEX_DIR),
        embeddings,
        allow_dangerous_deserialization=True,
    )