from celery import Celery
from sqlalchemy.future import select
import asyncio
from database.db import async_session_factory
from model.model import House

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def index_house(house_id):
    asyncio.run(index_house_task(house_id))

async def index_house_task(house_id):
    async with async_session_factory() as db:
        result = await db.execute(select(House).filter(House.id == house_id))
        house = result.scalar_one_or_none()
        if house: 
            await house.index_to_elasticsearch()

