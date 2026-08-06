import pytest
from pages.contact_page import ContactPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
contact_data = test_data["contact_data"]

def test_CT01_submit_contact_message(page):
    contact_page = ContactPage(page)
    page.goto("/contact_us")
    page.on("dialog", lambda dialog: dialog.accept()) #Clicks OK on JavaScript message
    contact_page.fill_contact_message(contact_data["name"], contact_data["email"], contact_data["subject"], contact_data["message"])
    assert contact_page.contact_success_message.is_visible()

@pytest.mark.skip(reason="Browser-native validation, not application logic. Covered at API level.")
def test_CT02_attempt_contact_submition_with_blank_email(page):
    pass