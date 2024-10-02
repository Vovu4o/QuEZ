from contextlib import asynccontextmanager
import time
import uvicorn
from fastapi import FastAPI, APIRouter, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from navec import Navec
from opinion_service.processing import get_keywords


MODELS = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    path = 'opinion_service/navec_hudlit_v1_12B_500K_300d_100q.tar'
    navec_model = Navec.load(path)
    MODELS["navec"] = navec_model
    yield


app = FastAPI(lifespan=lifespan, debug=True)
templates = Jinja2Templates(directory="templates")
opinion_router = APIRouter(prefix="/api")
site_router = APIRouter(prefix="/site")
@site_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@site_router.get("/upload_opinion", response_class=HTMLResponse)
async def upload_opinion(request: Request):
    return templates.TemplateResponse("upload_opinion.html", {"request": request})

@opinion_router.get("/")
async def api_index():
    return {"message": "ok!"}

@opinion_router.post("/upload_opinion")
async def api_upload_opinion_file(file: UploadFile):
    start = time.time()
    content = await file.read()
    ans = await get_keywords(content, MODELS["navec"])
    return {"time": time.time() - start, "opinion_keywords": ans}

app.include_router(opinion_router)
app.include_router(site_router)
origins = [
        "79.174.84.209"
        "127.0.0.1"
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )



