from pages.login_page import LoginPage
from utils.data_reader import read_json

test_data = read_json("test_data.json")
user_data = test_data["register_user_data"]

def test_DE01_delete_user(page, registered_user):
    login_page = LoginPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    login_page.click_on_delete_account ()
    assert login_page.account_deleted_message.is_visible()