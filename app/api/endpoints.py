from fastapi import Body

async def chat_endpoint(message: str = Body(..., embed=True)):
    return {
        "input": message,
        "response": f"You said: {message}"
    }

async def health_check():
    return {"status": "Healthy ✅"}