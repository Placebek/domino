from pydantic import BaseModel


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    phone_number: int

class UserBase(BaseModel):
    phone_number: int
    password: str