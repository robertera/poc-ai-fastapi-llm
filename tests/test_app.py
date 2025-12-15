import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_ask():
    response = client.post("/ask", json={"question": "Como faço login?"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "login" in data["context"]