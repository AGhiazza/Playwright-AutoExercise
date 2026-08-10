import pytest
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]

@pytest.mark.api
def test_US_user_account_lifecycle(playwright, base_url): #Cases US01 to US04 were combined as they follow a specific lifecycle.
    api = playwright.request.new_context(base_url=base_url)

    # Cleanup before test (in case user exists from previous run)
    api.delete("/api/deleteAccount", form={"email": user_data["email"], "password": user_data["password"]})
    
    # Create
    response = api.post("/api/createAccount", form={"name": user_data["name"], "email": user_data["email"], "password": user_data["password"], "firstname": user_data["firstname"], "lastname": user_data["lastname"], "address1": user_data["address"], "country": user_data["country"], "zipcode": user_data["zipcode"], "state": user_data["state"], "city": user_data["city"], "mobile_number": user_data["mobile"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 201
    
    # Update
    response = api.put("/api/updateAccount", form={"name": user_data["name"], "email": user_data["email"], "password": user_data["password"], "firstname": user_data["firstname"], "lastname": user_data["lastname"], "address": user_data["address"], "country": user_data["country"], "state": user_data["state"],  "city": user_data["city"], "zipcode": user_data["zipcode"], "mobile": user_data["mobile"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    
    # Get
    response = api.get("/api/getUserDetailByEmail", params={"email": user_data["email"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    
    # Delete
    response = api.delete("/api/deleteAccount", form={"email": user_data["email"], "password": user_data["password"]})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    
    api.dispose()