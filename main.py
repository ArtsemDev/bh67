from fastapi import FastAPI
from asyncio import sleep


app = FastAPI()


@app.get('/')
async def index():
    await sleep(0.5)
    return {'status': 'ok'}
