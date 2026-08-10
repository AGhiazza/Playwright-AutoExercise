import pytest
from pages.base_page import BasePage
from utils.logger import logger

@pytest.mark.ui
@pytest.mark.smoke
def test_smoke_navigation(page):
    base = BasePage(page)
    logger.info("Navigating to home page")
    page.goto("/")
    logger.info("Navigating to products page")
    base.navigate_to_products()
    logger.info("Verifying correct navigation")
    assert "/products" in page.url
    logger.info("Products page is displayed successfully")