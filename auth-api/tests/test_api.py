from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_public_info():
    response = client.get("/public/info")
    assert response.status_code == 200

def test_protected_without_token():
    response = client.get("/protected/profile")
    assert response.status_code == 401
