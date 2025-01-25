from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from model.model import House, SellerHouse, Photo, Address, City, District, Street, HousePhoto, Characteristic, HouseType
from app.api.houses.shemas.create import HouseCreate
from context.context import validate_access_token
from app.api.houses.shemas.response import HouseBase, HouseIDBase, SellerHouseBase, AddressAllBase, HouseTypeBase, CharacteristicBase, PhotoBase


async def create_house(request: HouseCreate, access_token: str, db: AsyncSession):
    user = await validate_access_token(access_token)
    new_house = House(
        name=request.name,
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

    for photo_data in request.photos:
        new_photo = Photo(photo_link=photo_data.photo_link)
        db.add(new_photo)
        await db.commit()  
        await db.refresh(new_photo)  

        house_photo = HousePhoto(house_id=new_house.id, photo_id=new_photo.id)
        db.add(house_photo)

    await db.commit()

    seller_house = SellerHouse(
        user_id=user["user_id"],
        house_id=new_house.id
    )
    db.add(seller_house)
    await db.commit()

    return {"message": "House created and linked with seller successfully", "house_id": new_house.id}


async def get_all_houses(db: AsyncSession, skip: int = 0, limit: int = 10):
    result = await db.execute(
        select(House)
        .options(
            joinedload(House.address)
            .joinedload(Address.city)
            .joinedload(City.district)
            .joinedload(District.street),
            joinedload(House.type),
            joinedload(House.characteristic),
            joinedload(House.house_photos).joinedload(HousePhoto.photo) 
        )
    )
    houses = result.unique().scalars().all()

    house_list = []
    for house in houses:
        house_dict = HouseBase.from_orm(house)
        house_list.append(house_dict)
    
    return house_list


async def get_house_by_id(db: AsyncSession, house_id: int):
    result = await db.execute(
        select(House)
        .options(
            joinedload(House.address)
            .joinedload(Address.city)
            .joinedload(City.district)
            .joinedload(District.street),
            joinedload(House.type),
            joinedload(House.characteristic),
            joinedload(House.house_photos).joinedload(HousePhoto.photo),
            joinedload(House.seller_houses).joinedload(SellerHouse.user)  # Load sellers with user data
        )
        .filter(House.id == house_id)
    )
    house = result.scalars().first()  # Fetch the first matching house

    if not house:
        raise HTTPException(status_code=404, detail="House not found")

    # Debug logging
    print(f"House {house.id} has seller_houses: {house.seller_houses}")

    # Serialize seller houses
    sellers = [
        SellerHouseBase(
            user=seller_house.user,
            house_id=seller_house.house_id
        )
        for seller_house in house.seller_houses
    ]

    # Serialize the full house object
    house_response = HouseBase(
        id=house.id,
        name=house.name,
        price=house.price,
        description=house.description,
        is_selled=house.is_selled,
        address=AddressAllBase.from_orm(house.address),
        type=HouseTypeBase.from_orm(house.type),
        characteristic=CharacteristicBase.from_orm(house.characteristic),
        photos=[PhotoBase.from_orm(photo.photo) for photo in house.house_photos],
        seller=sellers
    )

    return house_response