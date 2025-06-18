import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_record():
    payload = {
        "user_id": 555,
        "date": "2025-06-21",
        "steps": 12345
    }
    res = requests.post(f"{BASE_URL}/records", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert data["user_id"] == 555
    assert data["steps"] == 12345
    # Save ID for later
    global created_id
    created_id = data["id"]

def test_get_records():
    res = requests.get(f"{BASE_URL}/records")
    assert res.status_code == 200
    records = res.json()
    assert any(r["id"] == created_id for r in records)

def test_update_record():
    updated = {
        "user_id": 555,
        "date": "2025-06-22",
        "steps": 9999
    }
    res = requests.put(f"{BASE_URL}/records/{created_id}", json=updated)
    assert res.status_code == 200
    data = res.json()
    assert data["steps"] == 9999

def test_delete_record():
    res = requests.delete(f"{BASE_URL}/records/{created_id}")
    assert res.status_code == 200
    assert "deleted" in res.json()["detail"].lower()

    # Confirm it's gone
    res = requests.get(f"{BASE_URL}/records")
    assert res.status_code == 200
    assert all(r["id"] != created_id for r in res.json())
