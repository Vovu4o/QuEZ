from contextlib import asynccontextmanager
import time
import uvicorn
from fastapi import FastAPI, APIRouter, UploadFile, BackgroundTasks
from navec import Navec
from opinion_service.controllers import get_keywords


MODELS = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    path = 'opinion_service/navec_hudlit_v1_12B_500K_300d_100q.tar'
    navec_model = Navec.load(path)
    MODELS["navec"] = navec_model
    yield

def start_app(debug):

    app = FastAPI(lifespan=lifespan, debug=debug)
    opinion_router = APIRouter()

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

    app.include_router(opinion_router)
    return app



if __name__ == "__main__":
    app = start_app(True)
    uvicorn.run(app=app, host='127.0.0.1', port=8000)


