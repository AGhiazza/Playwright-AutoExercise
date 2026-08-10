import pytest
from pages.login_page import LoginPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
valid_user = test_data["valid_user"]
invalid_user = test_data["invalid_user"]

@pytest.mark.ui
def test_LO01_successful_login(page):
    login_page = LoginPage(page)
    logger.info("Navigating to login page")
    page.goto("/login")
    logger.info("Login in")
    login_page.login(valid_user["email"], valid_user["password"])
    username = login_page.get_logged_in_username() #Calls the method that gets the text in the "Logged in as *username*" locator
    logger.info("Comparing registered user name vs displayed user name")
    assert username == "John"
    logger.info("User name comparison successful")

@pytest.mark.skip(reason="Browser-native validation, not application logic. Covered at API level.")
def test_LO02_login_attempt_empty_fields(page):
    login_page = LoginPage(page)
    page.goto("/login")
    login_page.login_button.click()
    
@pytest.mark.ui
def test_LO03_login_attempt_wrong_credentials(page):
    login_page = LoginPage(page)
    logger.info("Navigating to login page")
    page.goto("/login")
    logger.info("Attempting login with wrong credentials")
    login_page.login(invalid_user["email"], invalid_user["password"])
    error_message = login_page.get_login_error_message()
    logger.info("Verifying login error message")
    assert error_message == "Your email or password is incorrect!"
    logger.info("Login error message is displayed successfully")

@pytest.mark.ui
def test_LO04_successful_logout(logged_in_page):
    login_page = LoginPage(logged_in_page)
    logger.info("Navigating to home page with logged user")
    logged_in_page.goto("/")
    logger.info("Login out")
    login_page.click_on_logout()
    logger.info("Veryfing logout button is not displayed anymore")
    assert not login_page.logout_button.is_visible()
    logger.info("Logout button is not displayed")
