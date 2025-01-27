from pydantic import BaseModel
from typing import List, Optional


class StreetBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True

class DistrictBase(BaseModel):
    id: int
    name: str
    street: StreetBase

    class Config:
        orm_mode = True
        from_attributes = True

class CityBase(BaseModel):
    id: int
    name: str
    district: DistrictBase

    class Config:
        orm_mode = True  
        from_attributes = True  

class AddressBase(BaseModel):
    id: int
    city: CityBase

    class Config:
        orm_mode = True
        from_attributes = True    

class AddressAllBase(BaseModel):
    id: int
    city: CityBase
    house_number: str
    apartment_number: int
    floor: int

    class Config:
        orm_mode = True
        from_attributes = True

class HouseTypeBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
        from_attributes = True

class CharacteristicBase(BaseModel):
    id: int
    count_room: int
    is_furnished: bool
    year_of_construction: int
    area: float

    class Config:
        orm_mode = True
        from_attributes = True

class PhotoBase(BaseModel):
    id: int
    photo_link: str

    class Config:
        orm_mode = True
        from_attributes = True
        
class HouseBase(BaseModel):
    id: int
    name: str
    price: int
    is_selled: bool
    address: AddressBase
    type: HouseTypeBase
    characteristic: CharacteristicBase
    photos: Optional[List[PhotoBase]] = []

    class Config:
        orm_mode: True  
        from_attributes = True
    
class UserBase(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: str
    phone_number: str
    photo: Optional[str] = None

    class Config:
        orm_mode = True
        from_attributes = True

class SellerHouseBase(BaseModel):
    user: UserBase
    house_id: int

    class Config:
        orm_mode = True
        from_attributes = True

class HouseIDBase(BaseModel):
    id: int
    name: str
    price: int
    is_selled: bool
    address: AddressAllBase
    type: HouseTypeBase
    characteristic: CharacteristicBase
    photos: Optional[List[PhotoBase]] = None
    description: str
    seller: Optional[List[SellerHouseBase]] = []

    class Config:
        orm_mode = True
        from_attributes = True