import pytest
from pages.products_page import ProductsPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("navigation_data.json")
valid_search_term = test_data["valid_search_term"]
invalid_search_term = test_data["invalid_search_term"]

@pytest.mark.ui
def test_PR01_search_for_product(page):
    logger.info("Starting test: test_")
    products_page = ProductsPage(page)
    page.goto("/products")
    products_page.search_for_product(valid_search_term)
    assert "SEARCHED PRODUCTS" in products_page.products_section_title.inner_text()
    assert products_page.product_cards.count() > 0

@pytest.mark.ui
def test_PR02_search_for_nonexisting_product(page):
    logger.info("Starting test: test_")
    products_page = ProductsPage(page)
    page.goto("/products")
    products_page.search_for_product(invalid_search_term)
    assert products_page.product_cards.count() == 0