from uuid import uuid4

from motor.motor_asyncio import AsyncIOMotorClient


class Mongo:

    def __init__(self):
        self.client = AsyncIOMotorClient("mongodb://admin:admin@mongo:27017/",
                                         maxPoolSize=10,
                                         minPoolSize=10)

    async def save_event(self, event):
        event["_id"] = str(uuid4())
        await self.client["webhook"]["events"].insert_one(event)
