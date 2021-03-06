from typing import Optional
from fastapi import FastAPI

from .routes.api.v1 import router

app = FastAPI()

app.include_router(router)