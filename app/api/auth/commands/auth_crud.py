from fastapi import HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from context.context import create_access_token, hash_password, verify_password
from app.api.auth.shemas.create import UserCreate, UserBase
from app.api.auth.shemas.response import TokenResponse
from model.model import User, Card


async def user_register(user: UserCreate, db: AsyncSession):
    stmt = await db.execute(
        select(User).filter(User.phone_number == user.phone_number)
    )
    existing_user = stmt.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = hash_password(user.password)

    new_user_stmt = await db.execute(
        insert(User).values(
            firstname = user.firstname,
            lastname = user.lastname,
            email = user.email,
            password = hash_password(user.password),
            phone_number = user.phone_number
        ).returning(User.id)
    )
    await db.commit()

    user_id = new_user_stmt.fetchone()[0]

    await db.execute(
        insert(Card).values(
            id=user_id,
            card_token=f"card_{user_id}"
        )
    )
    await db.commit()

    access_token, expire_time = create_access_token(data={"sub": str(user_id)})

    return TokenResponse(
        access_token=access_token,
        access_token_expire_time=expire_time
    )


async def user_login(user: UserBase, db: AsyncSession):
    stmt = await db.execute(
        select(User).filter(User.phone_number == user.phone_number)
    )
    db_user = stmt.scalar_one_or_none()

    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid phone number or password")
    
    access_token, expire_time = create_access_token(data={"sub": str(db_user.id)})

    return {
        "roles": "user",
        "access_token": access_token,
        "access_token_expire_time": expire_time
    }