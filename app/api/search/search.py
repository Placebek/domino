from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from app.api.search.commands.search_crud import search_houses
from app.api.search.shemas.response import HouseBase
from typing import Optional, List
# from app.api.houses.shemas.response import HouseBase


router = APIRouter()

@router.get("/houses", response_model=List[HouseBase])
async def search(
    query: str = Query(None, description="Full-text search query"),
    min_price: int = Query(None, description="Minimum price filter"),
    max_price: int = Query(None, description="Maximum price filter"),
    min_floor: int = Query(None, description="Minimum floor filter"),
    max_floor: int = Query(None, description="Maximum floor filter"),
    min_count_room: int = Query(None, description="Minimum number of rooms"),
    max_count_room: int = Query(None, description="Maximum number of rooms"),
    min_year_of_construction: int = Query(None, description="Minimum year of construction"),
    max_year_of_construction: int = Query(None, description="Maximum year of construction"),
    min_area: int = Query(None, description="Minimum area"),
    max_area: int = Query(None, description="Maximum area"),
    db: AsyncSession = Depends(get_db),
):
    houses = await search_houses(
        db=db,
        query=query,
        min_price=min_price,
        max_price=max_price,
        min_floor=min_floor,
        max_floor=max_floor,
        min_count_room=min_count_room,
        max_count_room=max_count_room,
        min_year_of_construction=min_year_of_construction,
        max_year_of_construction=max_year_of_construction,
        min_area=min_area,
        max_area=max_area,
    )

    return [HouseBase.from_orm(house[0]) for house in houses]