from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from app.api.auth.shemas.create import UserCreate, UserBase
from app.api.auth.shemas.response import TokenResponse
from app.api.auth.commands.auth_crud import user_register, user_login


router = APIRouter()

@router.post("/register", response_model=TokenResponse)
async def register(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_register(user=user, db=db)


@router.post("/login", response_model=dict)
async def login(user: UserBase, db: AsyncSession = Depends(get_db)):
    return await user_login(user=user, db=db)