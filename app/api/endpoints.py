from fastapi import Body
from app.services.document_loader import load_hr_documents

async def chat_endpoint(message: str = Body(..., embed=True)):
    return {
        "input": message,
        "response": f"You said: {message}"
    }

async def health_check():
    return {"status": "Healthy ✅"}



async def load_hr_policy():
    try:
        documents = load_hr_documents()

        return {
            "status": "Loaded Successfully",
            "total_pages": len(documents),
            "preview": documents[0].page_content[:300] if documents else "No content"
        }

    except Exception as e:
        return {"error": str(e)}
   
from app.services.document_loader import load_hr_documents
from app.services.text_splitter import split_documents

async def load_and_split_hr_policy():
    try:
        docs = load_hr_documents()
        chunks = split_documents(docs)

        return {
            "status": "Success",
            "total_pages": len(docs),
            "total_chunks": len(chunks),
            "first_chunk_preview": chunks[0].page_content[:300] if chunks else "No content"
        }

    except Exception as e:
        return {"error": str(e)}   