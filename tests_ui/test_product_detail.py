import pytest
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
review_data = test_data["review"]

@pytest.mark.ui
def test_PD01_write_a_review(page):
    products_page = ProductsPage (page)
    product_detail_page = ProductDetailPage(page)
    logger.info("Navigating to Products")
    page.goto("/products")
    logger.info("Navigating to first product's detail page")
    products_page.click_on_first_view_product_details()
    logger.info("Writting a review and submitting it")
    product_detail_page.write_a_review(review_data["name"], review_data["email"], review_data["review"])
    logger.info("Verifying review submission message")
    assert product_detail_page.successful_review_submission_message.is_visible()
    logger.info("Successful review submission message is displayed")