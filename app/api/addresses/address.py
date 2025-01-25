from fastapi import APIRouter, Depends
from app.api.addresses.shemas.create import AddressCreate
from database.db import get_db
from context.context import get_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.addresses.commands.address_crud import create_address, get_all_cities


router = APIRouter()

@router.post('/create-address')
async def create_address_view(request: AddressCreate, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await create_address(request=request, access_token=access_token, db=db)

@router.get('/cities')
async def list_cities(skip: int=0, limit: int=10, db: AsyncSession = Depends(get_db)):
    return await get_all_cities(db, skip, limit)