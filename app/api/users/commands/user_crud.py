from fastapi import HTTPException, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.model import User
from context.context import validate_access_token
import os


async def user_update_photo(file: UploadFile, access_token: str, db: AsyncSession):
    user = await validate_access_token(access_token)

    stmt = await db.execute(select(User).where(User.id == user["user_id"])) 
    user = stmt.scalars().first()  

    if not user:
        raise HTTPException(status_code=400, detail='User not found')

    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type. Only JPEG and PNG are allowed.")
    
    file_path = f"uploads/photos/{user.id}_{file.filename}"

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    user.photo = file_path
    db.add(user)
    await db.commit()

    return {"message": "Photo updated successfully", "photo_path": file_path}
