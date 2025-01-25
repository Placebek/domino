from pydantic import BaseModel
from typing import List, Optional


class PhotoCreate(BaseModel):
    id: int
    photo_link: str

class HouseCreate(BaseModel):
    name: str
    price: int
    description: str
    address_id: int
    type_id: int
    characteristic_id: int
    is_selled: Optional[bool] = False
    photos: List[PhotoCreate]

    class Config: 
        orm_mode = True