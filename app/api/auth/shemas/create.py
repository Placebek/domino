from pydantic import BaseModel


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    phone_number: str

class UserBase(BaseModel):
    phone_number: str
    password: str