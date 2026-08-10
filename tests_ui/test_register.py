import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]
valid_user = test_data["valid_user"]

@pytest.mark.ui
def test_RE01_register_new_user(page):
    login_page = LoginPage(page)
    register_page = RegisterPage (page)
    logger.info("Navigating to login page")
    page.goto("/login")
    logger.info("Beginning register process")
    login_page.signup(user_data["name"], user_data["email"])
    logger.info("Completing register information")
    register_page.fill_account_info(user_data["password"])
    register_page.fill_address_info(user_data["firstname"], user_data["lastname"], user_data["address"], user_data["country"], user_data["state"], user_data["city"], user_data["zipcode"], user_data["mobile"])
    logger.info("Submitting registration")
    register_page.click_on_create_account()
    logger.info("Verifying Account Created message is displayed")
    assert register_page.account_created_message.is_visible()
    logger.info("Account Created message is displayed successfully")
    logger.info("Deleting user account (teardown)")
    page.request.delete("https://automationexercise.com/api/deleteAccount", form={"email": user_data["email"], "password": user_data["password"]}) #Registered user teardown, if test fails, the data must be deleted manually
    

@pytest.mark.ui
def test_RE02_attempt_register_with_existing_email(page): 
    login_page = LoginPage(page)
    logger.info("Navigating to login page")
    page.goto("/login")
    logger.info("Attempting register process with existing email")
    login_page.signup(valid_user["name"], valid_user["email"])
    error_message = login_page.get_signup_error_message()
    logger.info("Verifying Existing email error message")
    assert error_message == "Email Address already exist!"
    logger.info("Error message is displaying successfully")