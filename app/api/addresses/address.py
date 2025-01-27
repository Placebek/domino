from fastapi import APIRouter, Depends
from database.db import get_db
from context.context import get_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.addresses.commands.address_crud import get_all_cities, get_districts_by_city, get_street_by_district
from typing import List
from app.api.addresses.shemas.response import DistrictBase, StreetBase


router = APIRouter()

@router.get('/cities')
async def list_cities(skip: int=0, limit: int=10, db: AsyncSession = Depends(get_db)):
    return await get_all_cities(db, skip, limit)

@router.get("/cities/{city_id}/districts", response_model=List[DistrictBase])
async def list_districts(city_id: int, db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    return await get_districts_by_city(city_id, db, skip, limit)

@router.get("/districts/{district_id}/streets", response_model=List[StreetBase])
async def list_streets(district_id: int, db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    return await get_street_by_district(district_id, db, skip, limit)