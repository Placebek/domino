from celery import Celery
from sqlalchemy.future import select
from sqlalchemy import func
import asyncio
from database.db import async_session_factory
from model.model import House

app = Celery("tasks", broker="redis://localhost:6379/0")

@app.task
def update_search_vector():
    asyncio.run(update_task())

async def update_task():
    async with async_session_factory() as db:
        stmt = select(House)
        result = await db.execute(stmt)
        houses = result.scalars().all()

        for house in houses:
            house.search_vector = func.to_tsvector(
                'russian',  
                f"{house.name} {house.description} {house.house_number}"
            )

        await db.commit()
