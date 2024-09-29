import uvicorn
from fastapi import FastAPI

from routes import router

def start_app():

    app = FastAPI()
    app.include_router(router)
    return app

if __name__ == "__main__":
    app = start_app()
    uvicorn.run(app=app, host='127.0.0.1', port=8989)


