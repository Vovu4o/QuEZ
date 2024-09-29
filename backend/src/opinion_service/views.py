import time
from fastapi import APIRouter, UploadFile, BackgroundTasks

from .controllers import get_keywords


router = APIRouter(prefix="/opinions")


@router.get("/")
async def index():
    return {"Message": "page of opinions"}

@router.post("/upload_opinion/")
async def upload_opinion_file(file: UploadFile, background_tasks: BackgroundTasks):
    start = time.time()
    content = await file.read()
    background_tasks.add_task(get_keywords, content)
    return {"filename": file.filename, "content_type": file.content_type, 'time': time.time() - start}