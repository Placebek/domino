from pydantic import BaseModel
from typing import Optional


class HouseCreate(BaseModel):
    price: int
    description: str
    address_id: int
    type_id: int
    characteristic_id: int
    is_selled: Optional[bool] = False
    photo: Optional[str] = None