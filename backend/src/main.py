import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import main_router

def start_app():

    app = FastAPI()
    app.include_router(main_router)
    app.middleware(
        CORSMiddleware(app,
        allow_origins=[
            "http://localhost:3000"
        ],
        allow_credentials=True,
        allow_methods="*",
        allow_headers="*"

    ))
    return app

if __name__ == "__main__":
    app = start_app()
    uvicorn.run(app=app, host='127.0.0.1', port=8000)


