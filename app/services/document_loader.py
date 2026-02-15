import os
from langchain_community.document_loaders import PyPDFLoader
def load_hr_documents():
    Base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    filepath = os.path.join(Base_dir,"data","nestle_hr_policy.pdf")
    loader = PyPDFLoader(filepath)
    documents = loader.load()
    return documents