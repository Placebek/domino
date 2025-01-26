from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from model.model import Address, District, Street, City
from app.api.addresses.shemas.create import AddressCreate
from app.api.addresses.shemas.response import CityBase, DistrictBase, StreetBase
from context.context import validate_access_token
from fastapi import HTTPException
from typing import List


async def create_address_with_relations(access_token: str, data: AddressCreate, db: AsyncSession):
    user = await validate_access_token(access_token)
    if not user:  
        raise HTTPException(status_code=401, detail="Invalid access token")
    
    city_result = await db.execute(select(City).filter(City.id == data.city_id))
    city = city_result.scalars().first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    district_result = await db.execute(select(District).filter(District.id == data.district_id))
    district = district_result.scalars().first()
    if not district:
        raise HTTPException(status_code=404, detail="District not found")

    if district.id != city.district_id:
        raise HTTPException(status_code=400, detail="District does not belong to the selected city")

    street_result = await db.execute(select(Street).filter(Street.id == data.street_id))
    street = street_result.scalars().first()
    if not street:
        raise HTTPException(status_code=404, detail="Street not found")

    if street.id != district.street_id:
        raise HTTPException(status_code=400, detail="Street does not belong to the selected district")

    new_address = Address(
        house_number=data.house_number,
        apartment_number=data.apartment_number,
        floor=data.floor,
        city_id=data.city_id,
        district_id=data.district_id,
        street_id=data.street_id
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


async def get_districts_by_city(city_id: int, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[DistrictBase]:
    city_result = await db.execute(select(City).filter(City.id == city_id))
    city = city_result.scalars().first()
    if not city:
        raise HTTPException(status_code=404, detail="City not found")

    result = await db.execute(
        select(District.id, District.name)
        .filter(District.street_id == city.district_id)
        .offset(skip)
        .limit(limit)
    )
    districts = result.all()

    return [DistrictBase(id=district.id, name=district.name) for district in districts]


async def get_street_by_district(district_id: int, db: AsyncSession, skip: int = 0, limit: int = 10) -> List[StreetBase]:
    distrist_result = await db.execute(select(District).filter(District.id == district_id))
    district = distrist_result.scalars().first()
    if not district:
        raise HTTPException(status_code=404, detail="District not found")

    result = await db.execute(
        select(Street.id, Street.name)
        .join(District, Street.id == District.street_id)
        .filter(District.id == district_id)
        .offset(skip)
        .limit(limit)
    )
    streets = result.all()

    return [StreetBase(id=street.id, name=street.name) for street in streets]