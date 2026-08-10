import pytest
from utils.logger import logger
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

@pytest.fixture(scope="session")
def auth_state(browser, base_url):
    context = browser.new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/login")
    page.locator("[data-qa='login-email']").fill(test_data["valid_user"]["email"])
    page.locator("[data-qa='login-password']").fill(test_data["valid_user"]["password"])
    page.locator("[data-qa='login-button']").click()
    page.wait_for_load_state("networkidle")
    context.storage_state(path="data/auth.json")
    context.close()
    return "data/auth.json"

@pytest.fixture
def logged_in_page(browser, base_url, auth_state):
    context = browser.new_context(base_url=base_url, storage_state=auth_state)
    page = context.new_page()
    yield page
    context.close()

def pytest_runtest_logreport(report): #hook for logging errors
    if report.failed:
        logger.error(f"FAILED: {report.nodeid}")