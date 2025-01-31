from pydantic import BaseModel


class HouseBase(BaseModel):
    id: int
    name: str
    price: int
    description: str
    house_number: str
    apartment_number: int
    floor: int
    count_room: int
    year_of_construction: int
    area: float
    search_rank: float

    class Config:
        orm_mode = True
        from_attributes = True