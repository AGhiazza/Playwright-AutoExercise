import pytest
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def test_RE01_register_new_user(page):
    login_page = LoginPage(page)
    register_page = RegisterPage (page)
    page.goto("/login")
    
    login_page.signup(name, email)
    register_page.fill_account_info(password)
    register_page.fill_address_info(name, lastname, address, country, state, city, zipcode, mobile)
    register_page.click_on_create_account()
    assert register_page.account_created_message.is_visible()

def test_RE02_attempt_register_with_existing_email(page):
