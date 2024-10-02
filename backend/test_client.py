import os
import requests
from fastapi.testclient import TestClient
from fastapi.requests import Request
from src.main import start_app


app = start_app(True)
client = TestClient(app)

def test_api_index():
    response = client.get("/api/")
    assert response.status_code == 200
    assert response.json() == {"message": "ok!"}

def test_api_upload_opinion():
    log_file = open("opinion_service/test.log", "a")
    for filename in os.listdir("opinion_service/test_sentences"):
        path = f"opinion_service/test_sentences/{filename}"
        r = requests.post(
            url="http://localhost:8888/api/upload_opinion/",
            files={"file": open(path)}
        )
        assert r.status_code == 200
        log_file.write(f"File: {filename} time of work: {r.json()['time']}\n")
        assert float(r.json()["time"]) < 6.0

    log_file.close()


def test_index(request: Request):
    response = client.get("/")
    assert response.status_code == 200

def test_upload_opinion():
    pass