from pydantic import BaseModel


class AddressCreate(BaseModel):
    city_id: int
    house_number: str
    apartment_number: int
    floor: int