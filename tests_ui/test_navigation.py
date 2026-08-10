import pytest
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("navigation_data.json")
categories = [(item["category"], item["subcategory"]) for item in test_data["categories"]]
brands = test_data["brands"]

@pytest.fixture
def page(context_no_ads):
    page = context_no_ads.new_page()
    yield page
    page.close()

@pytest.mark.ui
@pytest.mark.parametrize("category, subcategory", categories)
def test_NA01_navigate_to_category(page, category, subcategory):
    logger.info("Starting test: test_")
    products_page = ProductsPage(page)
    page.goto("/products")
    products_page.navigate_to_category(category, subcategory)
    breadcrumb_text = products_page.category_breadcrumb.inner_text()
    assert category in breadcrumb_text and subcategory in breadcrumb_text

@pytest.mark.ui
@pytest.mark.parametrize("brand", brands)
def test_NA02_navigate_to_brand(page, brand):
    logger.info("Starting test: test_")
    products_page = ProductsPage(page)
    page.goto("/products")
    products_page.click_on_brand(brand)
    breadcrumb_text = products_page.category_breadcrumb.inner_text()
    assert brand in breadcrumb_text

@pytest.mark.ui
def test_NA03_navigate_to_product_detail(page):
    logger.info("Starting test: test_")
    products_page = ProductsPage(page)
    product_detail_page = ProductDetailPage(page)
    page.goto("/products")
    products_page.click_on_first_view_product_details()
    assert product_detail_page.product_name.is_visible()