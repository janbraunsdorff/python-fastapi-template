from fastapi import FastAPI

from app.api.status import status_router
from app.api.user import user_router

api = FastAPI()

api.include_router(status_router)
api.include_router(user_router)
