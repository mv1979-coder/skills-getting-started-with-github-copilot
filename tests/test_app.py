from urllib.parse import quote

from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_delete_participant_unregisters_student():
    email = "michael@mergington.edu"
    activity = "Chess Club"

    response = client.delete(f"/activities/{activity}/participants/{quote(email)}")

    assert response.status_code == 200
    assert email not in response.json()["participants"]


def test_delete_participant_returns_404_for_missing_participant():
    activity = "Chess Club"
    email = "missing@mergington.edu"

    response = client.delete(f"/activities/{activity}/participants/{quote(email)}")

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found"
