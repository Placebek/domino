from fastapi import APIRouter
from app.api.auth.auth import router as auth_router
from app.api.houses.houses import router as house_router
from app.api.users.user import router as user_router
from app.api.addresses.address import router as address_router


route = APIRouter()

route.include_router(auth_router, prefix="/auth", tags=["Authentication"])
route.include_router(house_router, prefix="/house", tags=["House"])
route.include_router(user_router, prefix="/user", tags=["User"])
route.include_router(address_router, prefix="/address", tags=["Address"])