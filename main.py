from fastapi import FastAPI
from fastapi.openapi.models import HTTPBearer as HTTPBearerModel
from fastapi.middleware.cors import CORSMiddleware
from app.router import route


app = FastAPI()

origins = [
        # "http://localhost:3000",
    # "http://172.20.10.3:3000", 
    # "http://172.25.192.1:3000", 
    # "https://172.20.10.8:3000",
    # "https://localhost:3000/",
    # "https://172.25.192.1:3000/",
    # "https://192.168.193.31:3000/",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(route)