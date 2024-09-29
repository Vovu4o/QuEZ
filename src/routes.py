from fastapi import APIRouter


router = APIRouter()


@router.get("/router")
async def index():
    return {"message": "website works. Ok!"}