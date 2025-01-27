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
    if not user:
        raise HTTPException(status_code=401, detail="Invalid access token")
    
    new_house = House(
        name=request.name,
        price=request.price,
        description=request.description,
        house_number=request.house_number,
        apartment_number=request.apartment_number,
        floor=request.floor,
        type_id=request.type_id,
        city_id=request.city_id,
        district_id=request.district_id,
        street_id=request.street_id,
        count_room=request.count_room,
        is_furnished=request.is_furnished,
        year_of_construction=request.year_of_construction,
        area=request.area,
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
            joinedload(House.city).joinedload(City.district).joinedload(District.street),
            joinedload(House.type),
            joinedload(House.house_photos).joinedload(HousePhoto.photo),
        )
        .offset(skip)
        .limit(limit)
    )
    houses = result.scalars().unique().all()

    house_list = []
    for house in houses:
        house_dict = {
            "id": house.id,
            "name": house.name,
            "price": house.price,
            "is_selled": house.is_selled,
            "address": {
                "id": house.city.id if house.city else None,
                "city": {
                    "id": house.city.id if house.city else None,
                    "name": house.city.name if house.city else None,
                    "district": {
                        "id": house.city.district.id if house.city and house.city.district else None,
                        "name": house.city.district.name if house.city and house.city.district else None,
                        "street": {
                            "id": house.city.district.street.id if house.city and house.city.district and house.city.district.street else None,
                            "name": house.city.district.street.name if house.city and house.city.district and house.city.district.street else None,
                        } if house.city and house.city.district and house.city.district.street else None,
                    } if house.city and house.city.district else None,
                } if house.city else None,
            },
            "type": {
                "id": house.type.id if house.type else None,
                "name": house.type.name if house.type else None,
            },
            "characteristic": {
                "id": house.id,  # Assuming the characteristic ID is the same as the house ID
                "count_room": house.count_room,
                "is_furnished": house.is_furnished,
                "year_of_construction": house.year_of_construction,
                "area": house.area,
            },
            "photos": [
                {"id": photo.photo.id, "photo_link": photo.photo.photo_link}
                for photo in house.house_photos
            ],
        }

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