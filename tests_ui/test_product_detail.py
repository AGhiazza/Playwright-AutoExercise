import pytest
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
review_data = test_data["review"]

@pytest.mark.ui
def test_PD01_write_a_review(page):
    products_page = ProductsPage (page)
    product_detail_page = ProductDetailPage(page)
    page.goto("/products")
    products_page.click_on_first_view_product_details()
    product_detail_page.write_a_review(review_data["name"], review_data["email"], review_data["review"])
    assert product_detail_page.successful_review_submission_message.is_visible()