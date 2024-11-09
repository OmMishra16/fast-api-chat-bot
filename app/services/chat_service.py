from openai import OpenAI
from app.core.config import settings
from app.models.chat import ChatMessage, ChatConversation
from typing import List, Optional

client = OpenAI(api_key=settings.OPENAI_API_KEY)

MAX_CONTEXT_MESSAGES = 10;

async def get_chat_response(message: str, conversation_id: Optional[int] = None, conversations: List[ChatConversation] = None) -> str:

    messages = [{
        "role": "system",
        "content": "You are a helpful AI assistant. Maintain context of the conversation but keep responses concise."
    }]
    

    if conversation_id and conversations:
        for conv in conversations:
            if conv.id == conversation_id:
                
                recent_messages = conv.messages[-MAX_CONTEXT_MESSAGES:]
                messages.extend([
                    {"role": msg.role.value, "content": msg.content}
                    for msg in recent_messages
                ])
                break
    

    messages.append({"role": "user", "content": message})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content
