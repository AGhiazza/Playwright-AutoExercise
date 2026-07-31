import pytest
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]

@pytest.fixture #Fixture for creating a user before running a test and deleting it afterwards
def registered_user(page):
    # Setup — Creates a user via API
    page.request.post("https://automationexercise.com/api/createAccount", form={
        "name": user_data["name"], 
        "email": user_data["email"], 
        "password": user_data["password"], 
        "firstname": user_data["firstname"], 
        "lastname": user_data["lastname"], 
        "address1": user_data["address"], 
        "country": user_data["country"], 
        "zipcode": user_data["zipcode"], 
        "state": user_data["state"], 
        "city": user_data["city"], 
        "mobile_number": user_data["mobile"]})
    
    yield  # Test Run
    
    # Teardown — Deletes the user via API
    page.request.delete("https://automationexercise.com/api/deleteAccount", form={"email": user_data["email"], "password": user_data["password"]})

@pytest.fixture
def context_no_ads(browser, base_url):
    context = browser.new_context(base_url=base_url)
    ad_domains = [
        "**/googlesyndication.com/**",
        "**/doubleclick.net/**",
        "**/google-analytics.com/**",
        "**/googletagmanager.com/**",
        "**/adservice.google.com/**",
        "**/media.net/**",
        "**/amazon-adsystem.com/**", 
        "**/adsystem.com/**",
        "**/pagead/**",
    ]
    for pattern in ad_domains:
        context.route(pattern, lambda route: route.abort())
    yield context
    context.close()