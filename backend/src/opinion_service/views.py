import os
import time
from fastapi import APIRouter, UploadFile
from navec import Navec

from .controllers import get_keywords
from routes import main_router as opinion_router
from main import MODELS, main_router as opinion_router

opinion_router
@opinion_router.get("/")
async def index():
    return {"Message": "page of opinions"}

@opinion_router.post("/upload_opinion/")
async def upload_opinion_file(file: UploadFile, background_tasks: BackgroundTasks):
    start = time.time()
    content = await file.read()
    # background_tasks.add_task(get_keywords, content, navec)
    ans = await get_keywords(content, MODELS["navec"])
    return {"result": time.time() - start, "ans": ans}