import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from utils.data_reader import read_json

test_data = read_json("test_data.json")
user_data = test_data["register_user_data"]

def test_RE01_register_new_user(page):
    login_page = LoginPage(page)
    register_page = RegisterPage (page)
    page.goto("/login")
    
    login_page.signup(user_data["name"], user_data["email"])
    register_page.fill_account_info(user_data["password"])
    register_page.fill_address_info(user_data["firstname"], user_data["lastname"], user_data["address"], user_data["country"], user_data["state"], user_data["city"], user_data["zipcode"], user_data["mobile"])
    register_page.click_on_create_account()
    assert register_page.account_created_message.is_visible()
    page.request.delete("https://automationexercise.com/api/deleteAccount", form={"email": user_data["email"], "password": user_data["password"]})


'''
def test_RE02_attempt_register_with_existing_email(page): # CAPAZ SEA UN CASO DE LOGINPAGE?
    login_page = LoginPage(page)
    register_page = RegisterPage (page)
    page.goto("/login")
    login_page.signup(name, email)
    error_message = login_page.get_signup_error_message()
    assert error_message == ""

'''