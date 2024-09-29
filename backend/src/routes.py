from fastapi import APIRouter
from opinion_service.views import router as opinion_router

main_router = APIRouter()
main_router.include_router(opinion_router)