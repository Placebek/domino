from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from model.model import Address, District, Street, City
from app.api.addresses.shemas.create import AddressCreate
from app.api.addresses.shemas.response import CityBase
from context.context import validate_access_token
from fastapi import HTTPException


async def create_address(request: AddressCreate, access_token: str, db: AsyncSession):
    user = await validate_access_token(access_token)
    if not user:  
        raise HTTPException(status_code=401, detail="Invalid access token")
    
    new_address = Address(
        city_id=request.city_id,
        house_number=request.house_number,
        apartment_number=request.apartment_number,
        floor=request.floor
    )

    db.add(new_address)
    await db.commit()
    await db.refresh(new_address)

    return {"message": "Address created successfully", "address_id": new_address.id}


async def get_all_cities(db: AsyncSession, skip: int=0, limit: int=10):
    result = await db.execute(
        select(City.id, City.name)
        .offset(skip)
        .limit(limit)    
    )
    cities = result.all()

    return [CityBase(id=city.id, name=city.name) for city in cities]