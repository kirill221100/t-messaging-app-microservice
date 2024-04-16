import datetime
from pydantic import BaseModel, ConfigDict
from typing import List, Optional
from db.models.chat import ChatTypes
from schemes.user import UserResponseScheme


class GroupChatScheme(BaseModel):
    users_ids: List[int]
    name: str


class DirectChatScheme(BaseModel):
    user_id: int


class ChatResponseScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    type: ChatTypes
    date_of_creation: datetime.datetime


class DirectChatResponseScheme(ChatResponseScheme):
    first_user: Optional[UserResponseScheme] = None
    second_user: Optional[UserResponseScheme] = None


class GroupChatResponseScheme(ChatResponseScheme):
    name: str
    creator_id: int