from fastapi.testclient import TestClient 
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health") #simulates get request 
    
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

def test_invalid_limit():
    response = client.get("/reports?limit=101")

    assert response.status_code == 422

def test_invalid_offset():
    response = client.get("/reports?offset=-1")
    
    assert response.status_code == 422

def test_invalid_status():
    response = client.get("/reports?status=banana")
    
    assert response.status_code == 422

def test_filter_by_status():
    response = client.get("/reports?status=approved")
    
    assert response.status_code == 200
    
    reports = response.json()
    
    for report in reports: 
        assert report["status"] == "approved"

def test_pagination():
    response = client.get("/reports?limit=2&offset=0")
    
    assert response.status_code == 200
    
    reports = response.json()
    
    assert len(reports) <= 2
