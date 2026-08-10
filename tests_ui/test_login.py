import pytest
from pages.login_page import LoginPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")

@pytest.mark.ui
def test_LO01_successful_login(page):
    logger.info("Starting test: test_")
    login_page = LoginPage(page)
    page.goto("/login")
    valid_user = test_data["valid_user"]
    login_page.login(valid_user["email"], valid_user["password"])
    username = login_page.get_logged_in_username() #Calls the method that gets the text in the "Logged in as *username*" locator
    assert username == "John"

@pytest.mark.skip(reason="Browser-native validation, not application logic. Covered at API level.")
def test_LO02_login_attempt_empty_fields(page):
    logger.info("Starting test: test_")
    login_page = LoginPage(page)
    page.goto("/login")
    login_page.login_button.click()
    
@pytest.mark.ui
def test_LO03_login_attempt_wrong_credentials(page):
    logger.info("Starting test: test_")
    login_page = LoginPage(page)
    page.goto("/login")
    invalid_user = test_data["invalid_user"]
    login_page.login(invalid_user["email"], invalid_user["password"])
    error_message = login_page.get_login_error_message()
    assert error_message == "Your email or password is incorrect!"

@pytest.mark.ui
def test_LO04_successful_logout(logged_in_page):
    logger.info("Starting test: test_")
    login_page = LoginPage(logged_in_page)
    logged_in_page.goto("/")
    login_page.click_on_logout()
    assert not login_page.logout_button.is_visible()
