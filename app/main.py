from fastapi import FastAPI
from app.api.routes.chat import router as chat_router

app = FastAPI(title="Chatbot API", version="1.0.0")

app.include_router(chat_router, prefix="/api/chat", tags=["chat"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Chatbot API"}