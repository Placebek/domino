from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: Optional[str] = None
    card_id: Optional[int] = None

class User(BaseModel):
    user_id: int
    first_name: str
    last_name: str
    email: str
    phone_number: Optional[str] = None
    card_id: Optional[int] = None

    class Config:
        orm_mode = True
