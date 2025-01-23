from fastapi import APIRouter, Depends
from app.api.houses.shemas.create import HouseCreate
from database.db import get_db
from context.context import get_access_token
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter()


@router.post("/create-house")
async def create_house(request: HouseCreate, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await create_house(request=request, access_token=access_token, db=db)