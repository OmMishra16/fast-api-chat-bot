from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"

class ChatMessage(BaseModel):
    id: Optional[int] = None
    role: Role
    content: str
    timestamp: datetime = datetime.now()

class ChatConversation(BaseModel):
    id: Optional[int] = None
    messages: List[ChatMessage] = []
    created_at: datetime = datetime.now()
