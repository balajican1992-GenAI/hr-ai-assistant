from fastapi import FastAPI
from app.api.router import router
app = FastAPI(title = "HR AI Assistant API", version = "1.0")

 

app.include_router(router)
@app.get("/")
def root():
    return {"message": "GenAI API is running 🚀"}