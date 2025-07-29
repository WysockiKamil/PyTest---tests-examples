import pytest
import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def load_email_test_data_from_json(path="test_data.json"):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return [(case["email"], case["status_code"], case["expected_valid"]) for case in data]      


@pytest.mark.parametrize("email, status_code, expected_valid", load_email_test_data_from_json())
def test_validate_email_from_json(email, status_code, expected_valid):
    response = client.post("/validate-email", json={"email": email})
    assert response.status_code == status_code

    if status_code == 200:
        assert response.json()["valid"] is expected_valid
        assert response.json()["email"] == email
    else:
        assert "valid" not in response.json()


