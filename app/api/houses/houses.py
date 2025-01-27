from fastapi import APIRouter, Depends, UploadFile, File, Form
from app.api.houses.shemas.create import HouseCreate, PhotoCreate
from app.api.houses.shemas.response import HouseBase, HouseIDBase, HouseTypeBase
from database.db import get_db
from context.context import get_access_token
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.houses.commands.houses_crud import (
    get_all_houses, create_house, 
    get_house_by_id, get_all_house_types
    )


router = APIRouter()

@router.post("/create-house")
async def create_house_view(
    name: str = Form(...),
    price: int = Form(...),
    description: str = Form(...),
    house_number: str = Form(...),
    apartment_number: int = Form(None),
    floor: int = Form(None),
    type_id: int = Form(...),
    city_id: int = Form(...),
    district_id: int = Form(...),
    street_id: int = Form(...),
    count_room: int = Form(...),
    is_furnished: bool = Form(...),
    year_of_construction: int = Form(...),
    area: float = Form(...),
    photos: list[UploadFile] = File(...),
    access_token: str = Depends(get_access_token),
    db: AsyncSession = Depends(get_db),
):
    photo_links = []
    for photo in photos:
        file_location = f"uploads/photos_house/{photo.filename}"
        with open(file_location, "wb") as file:
            file.write(await photo.read())
        photo_links.append(PhotoCreate(photo_link=file_location)) 

    request = HouseCreate(
        name=name,
        price=price,
        description=description,
        house_number=house_number,
        apartment_number=apartment_number,
        floor=floor,
        type_id=type_id,
        city_id=city_id,
        district_id=district_id,
        street_id=street_id,
        count_room=count_room,
        is_furnished=is_furnished,
        year_of_construction=year_of_construction,
        area=area,
        photos=photo_links,
    )

    return await create_house(request=request, access_token=access_token, db=db)

#/get-houses?skip=10&limit=10
@router.get("/get-houses", response_model=list[HouseBase])
async def get_houses(db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 10):
    houses = await get_all_houses(db, skip=skip, limit=limit)
    return houses

@router.get("/get-house/{house_id}", response_model=HouseIDBase)
async def get_house(house_id: int, db: AsyncSession = Depends(get_db)):
    house = await get_house_by_id(db, house_id)
    return HouseIDBase.from_orm(house)

@router.get("/get-house_types", response_model=list[HouseTypeBase])
async def get_house_types(skip: int=0, limit: int=10, db: AsyncSession=Depends(get_db)):
    house_types = await get_all_house_types(db, skip=skip, limit=limit)
    return house_types