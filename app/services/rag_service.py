from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.services.vector_store import get_vector_store

def get_rag_chain():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0
    )

    vector_store = get_vector_store()

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    prompt_template = """
You are a professional HR assistant.

Use the provided context to answer the question clearly.


Context:
{context}

Question:
{question}

Answer:
"""

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    rag_chain = (
        {
            "context": lambda x: format_docs(retriever.invoke(x["question"])),
            "question": lambda x: x["question"]
        }
        | PROMPT
        | llm
        | StrOutputParser()
    )

    return rag_chain


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def debug_retrieval(question, retriever):
    docs = retriever.invoke(question)

    print("\n===== RETRIEVED DOCS =====\n")
    for i, doc in enumerate(docs):
        print(f"\n--- Doc {i} ---\n")
        print(doc.page_content)

    return format_docs(docs)