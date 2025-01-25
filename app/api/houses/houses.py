from fastapi import APIRouter, Depends
from app.api.houses.shemas.create import HouseCreate
from app.api.houses.shemas.response import HouseBase, HouseIDBase
from database.db import get_db
from context.context import get_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.houses.commands.houses_crud import get_all_houses, create_house, get_house_by_id


router = APIRouter()

@router.post("/create-house")
async def create_house_view(request: HouseCreate, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await create_house(request=request, access_token=access_token, db=db)

#/get-houses?skip=10&limit=10
@router.get("/get-houses", response_model=list[HouseBase])
async def get_houses(db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    houses = await get_all_houses(db)
    return houses

@router.get("/get-house/{house_id}", response_model=HouseIDBase)
async def get_house(house_id: int, db: AsyncSession = Depends(get_db)):
    house = await get_house_by_id(db, house_id)
    return HouseIDBase.from_orm(house)