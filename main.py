from fastapi import FastAPI, Request

from db import Mongo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def webhook(req: Request):
    mongo = Mongo()
    event = await req.json()
    await mongo.save_event(event)
    return event
