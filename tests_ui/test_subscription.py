import pytest
from pages.base_page import BasePage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
subscription_email = test_data["subscription_email"]

@pytest.mark.ui
def test_SU01_subscribe(page):
    logger.info("Starting test: test_")
    base_page = BasePage(page)
    page.goto("/")
    base_page.subscribe(subscription_email)
    assert base_page.subscription_success_message.is_visible()