from fastapi import APIRouter
from app.api.auth.auth import router as auth_router
from app.api.houses.houses import router as house_router


route = APIRouter()

route.include_router(auth_router, prefix="/auth", tags=["Authentication"])
route.include_router(house_router, prefix="/house", tags=["House"])