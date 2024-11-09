from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from app.models.chat import ChatMessage, ChatConversation, Role
from app.services.chat_service import get_chat_response

router = APIRouter()

conversations: List[ChatConversation] = []

class MessageRequest(BaseModel):
    message: str

@router.post("/send")
async def send_message(request: MessageRequest, conversation_id: Optional[int] = None):
    try:

        bot_response = await get_chat_response(request.message, conversation_id, conversations)
        

        conversation = None
        if conversation_id:
            conversation = next((c for c in conversations if c.id == conversation_id), None)
        
        if not conversation:
            conversation = ChatConversation(id=len(conversations) + 1)
            conversations.append(conversation)
        
    
        user_message = ChatMessage(role=Role.USER, content=request.message)
        assistant_message = ChatMessage(role=Role.ASSISTANT, content=bot_response)
        conversation.messages.extend([user_message, assistant_message])
        
        return {
            "conversation_id": conversation.id,
            "user_message": request.message,
            "bot_response": bot_response
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))