from sqlalchemy import or_, func
from sqlalchemy.ext.asyncio import AsyncSession
from model.model import House


async def search_houses(
    db: AsyncSession, query: str=None, min_price: int=None, max_price: int=None,
    min_floor: int=None, max_floor: int=None, min_count_room: int=None, max_count_room: int=None,
    min_year_of_construction: int=None, max_year_of_construction: int=None, 
    min_area: int=None, max_area: int=None,
):
    filters = []
    if query:
        filters.append(House.search_vector.op('@@')(func.to_tsquery('russian', query)))
    if min_price is not None:
        filters.append(House.price >= min_price)
    if max_price is not None:
        filters.append(House.price <= max_price)
    if min_floor is not None:
        filters.append(House.floor >= min_floor)
    if max_floor is not None:
        filters.append(House.floor <= max_floor)
    if min_count_room is not None:
        filters.append(House.count_room >= min_count_room)
    if max_count_room is not None:
        filters.append(House.count_room <= max_count_room)
    if min_year_of_construction is not None:
        filters.append(House.year_of_construction >= min_year_of_construction)
    if max_year_of_construction is not None:
        filters.append(House.year_of_construction <= max_year_of_construction)
    if min_area is not None:
        filters.append(House.area >= min_area)
    if max_area is not None:
        filters.append(House.area <= max_area)

    stmt = db.query(House).filter(*filters)
    result = await db.execute(stmt)
    return result.scalars().all()