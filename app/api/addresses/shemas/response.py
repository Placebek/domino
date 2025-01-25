from pydantic import BaseModel
from typing import List


class DistrictBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True

class CityBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True

class StreetBase(BaseModel):
    id: int
    name: str