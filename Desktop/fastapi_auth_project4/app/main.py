from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, database

app = FastAPI()

@app.get("/users")
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users
