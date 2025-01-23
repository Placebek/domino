from fastapi import APIRouter
from app.api.auth.auth import router as auth_router


route = APIRouter()

route.include_router(auth_router, prefix="/auth", tags=["Authentication"])