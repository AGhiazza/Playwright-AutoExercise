import pytest
from utils.data_reader import read_json

test_data = read_json("user_data.json")
valid_user = test_data["valid_user"]
invalid_user = test_data["invalid_user"]

@pytest.mark.api
def test_AU01_valid_login(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/verifyLogin", form={"email":valid_user["email"], "password":valid_user["password"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    api.dispose()

@pytest.mark.api
def test_AU02_login_no_email(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/verifyLogin", data={"password":valid_user["password"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    api.dispose()

@pytest.mark.api
def test_AU03_delete_to_verify_login(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.delete("/api/verifyLogin", data={"email":valid_user["email"], "password":valid_user["password"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 405
    api.dispose()

@pytest.mark.api
def test_AU04_invalid_login(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/verifyLogin", form={"email":invalid_user["email"], "password":invalid_user["password"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 404
    api.dispose()
