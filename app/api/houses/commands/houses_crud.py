from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from model.model import House, SellerHouse, User
from shemas.create import HouseCreate
from context.context import validate_access_token, get_access_token


async def create_house(request: HouseCreate, access_token: str, db: AsyncSession):
    user = await validate_access_token(access_token)

    new_house = House(
        price=request.price,
        description=request.description,
        is_selled=request.is_selled,
        address_id=request.address_id,
        type_id=request.type_id,
        characteristic_id=request.characteristic_id
    )

    db.add(new_house)
    await db.commit()
    await db.refresh(new_house)

    seller_house = SellerHouse(
        user_id=user.id,
        house_id=new_house.id
    )
    
    db.add(seller_house)
    await db.commit()
    
    return {"message": "House created and linked with seller successfully", "house_id": new_house.id}


