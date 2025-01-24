from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from database.db import get_db
from context.context import get_access_token
from app.api.users.commands.user_crud import user_update_photo


router = APIRouter()

@router.patch('/update-photo')
async def update_photo(file: UploadFile, access_token: str = Depends(get_access_token), db: AsyncSession = Depends(get_db)):
    return await user_update_photo(file=file, access_token=access_token, db=db)