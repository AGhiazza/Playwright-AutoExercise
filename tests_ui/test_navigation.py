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
    products_page = ProductsPage(page)
    logger.info("Navigating to products page")
    page.goto("/products")
    logger.info("Navigating to category")
    products_page.navigate_to_category(category, subcategory)
    breadcrumb_text = products_page.category_breadcrumb.inner_text()
    logger.info("Verifying category and subcategory breadcrumb text")
    assert category in breadcrumb_text and subcategory in breadcrumb_text
    logger.info("Category and subcategory are successfully displayed in the breadcrumb text")

@pytest.mark.ui
@pytest.mark.parametrize("brand", brands)
def test_NA02_navigate_to_brand(page, brand):
    products_page = ProductsPage(page)
    logger.info("Navigating to products page")
    page.goto("/products")
    logger.info("Navigating to brand")
    products_page.click_on_brand(brand)
    breadcrumb_text = products_page.category_breadcrumb.inner_text()
    logger.info("Verifying brand breadcrumb text")
    assert brand in breadcrumb_text
    logger.info("Brand is successfully displayed in the breadcrumb text")

@pytest.mark.ui
def test_NA03_navigate_to_product_detail(page):
    products_page = ProductsPage(page)
    product_detail_page = ProductDetailPage(page)
    logger.info("Navigating to products page")
    page.goto("/products")
    logger.info("Navigating to first product's detail page")
    products_page.click_on_first_view_product_details()
    logger.info("Verifying successful navigation")
    assert product_detail_page.product_name.is_visible()
    logger.info("Product's detail page is displayed")