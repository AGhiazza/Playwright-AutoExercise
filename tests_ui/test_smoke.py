import pytest
from pages.base_page import BasePage
from utils.logger import logger

@pytest.mark.ui
@pytest.mark.smoke
def test_smoke_navigation(page):
    logger.info("Starting test: test_")
    base = BasePage(page)
    page.goto("/")
    base.navigate_to_products()
    assert "/products" in page.url