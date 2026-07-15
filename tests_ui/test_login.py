import pytest
from pages.login_page import LoginPage

@pytest.mark.ui
def test_LO01_successful_login(page):
    login_page = LoginPage(page)
    page.goto("https://automationexercise.com/login")
    login_page.login("aghiazzabna@gmail.com","Test")
    username = login_page.get_logged_in_username() #Calls the method that gets the text in the "Logged in as *username*" locator
    assert username == "Cosme fulano"

'''
def test_LO02_login_attempt_empty_fields(page):
    login_page = LoginPage(page)


def test_LO03_login_attempt_wrong_credentials(page):
    login_page = LoginPage(page)

def test_LO04_successful_logout(page):
    login_page = LoginPage(page)
    '''    