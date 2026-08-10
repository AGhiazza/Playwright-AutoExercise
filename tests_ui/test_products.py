import pytest
from pages.products_page import ProductsPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("navigation_data.json")
valid_search_term = test_data["valid_search_term"]
invalid_search_term = test_data["invalid_search_term"]

@pytest.mark.ui
def test_PR01_search_for_product(page):
    products_page = ProductsPage(page)
    logger.info("Navigating to products page")
    page.goto("/products")
    logger.info("Searching for a valid product")
    products_page.search_for_product(valid_search_term)
    logger.info("Verifying search results")
    assert "SEARCHED PRODUCTS" in products_page.products_section_title.inner_text()
    assert products_page.product_cards.count() > 0
    logger.info("Search is displaying results successfully")

@pytest.mark.ui
def test_PR02_search_for_nonexisting_product(page):
    products_page = ProductsPage(page)
    logger.info("Navigating to products page")
    page.goto("/products")
    logger.info("Searching for an invalid product")
    products_page.search_for_product(invalid_search_term)
    logger.info("Verifying search results")
    assert products_page.product_cards.count() == 0
    logger.info("Search is not displaying any results")
