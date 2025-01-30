from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from app.api.search.commands.search_crud import search_houses
from app.api.search.shemas.response import HouseBase
from typing import Optional, List
# from app.api.houses.shemas.response import HouseBase
from elastic_search_config import es


router = APIRouter()

@router.get("/houses")
async def search_houses(
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
    es_query = {"bool": {"must": [], "filter": []}}

    if query:
        es_query["bool"]["must"].append({"match": {"name": query}})
    
    if min_price:
        es_query["bool"]["filter"].append({"range": {"price": {"gte": min_price}}})
    if max_price:
        es_query["bool"]["filter"].append({"range": {"price": {"lte": max_price}}})

    results = await es.search(index="houses", query=es_query)
    return [hit["_source"] for hit in results["hits"]["hits"]]