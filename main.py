from fastapi import FastAPI, WebSocket
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware import Middleware
import uvicorn
import asyncio
from datetime import datetime
from routes import index
from fastapi_utils.tasks import repeat_every
from constants import *

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
        expose_headers=["Access-Control-Allow-Origin"]
    )
]

app = FastAPI(middleware=middleware)


app.include_router(index.router)

event_loop = asyncio.get_event_loop()


class BackgroundRunner:
    def __init__(self):
        pass

    async def run_main(self):
        pass


runner = BackgroundRunner()


async def eventLoopStart():
    pass


@app.on_event('startup')
@repeat_every(seconds=21600, raise_exceptions=True)
async def app_startup():
    await eventLoopStart()
    pass


if __name__ == "__main__":
    pass
