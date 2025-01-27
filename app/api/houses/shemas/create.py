from pydantic import BaseModel
from typing import List, Optional


class PhotoCreate(BaseModel):
    photo_link: str

class HouseCreate(BaseModel):
    name: Optional[str] = None
    price: int
    description: str
    house_number: str
    apartment_number: Optional[int] = None
    floor: Optional[int] = None
    type_id: int
    city_id: int
    district_id: int
    street_id: int
    count_room: int
    is_furnished: bool
    year_of_construction: int
    area: float
    photos: List[PhotoCreate]

    class Config: 
        orm_mode = True