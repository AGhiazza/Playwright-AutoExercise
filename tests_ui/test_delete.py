from pages.login_page import LoginPage

def test_DE01_delete_user(logged_in_page, registered_user):
    login_page = LoginPage(logged_in_page)
    logged_in_page.goto("/")
    login_page.click_on_delete_account()
    assert login_page.account_deleted_message.is_visible()