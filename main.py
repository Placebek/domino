from fastapi import FastAPI
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.router import route


app = FastAPI()

media_folder = "media/"
app.mount("/media", StaticFiles(directory=media_folder), name="media")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(route)