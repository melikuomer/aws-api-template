from sys import prefix
from fastapi import APIRouter
api_router = APIRouter()


from .ping import router as health_route


api_router.include_router(health_route,prefix="/ping")






__all__=["api_router"]
