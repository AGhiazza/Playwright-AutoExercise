import pytest
from pages.products_page import ProductsPage
from utils.data_reader import read_json

test_data = read_json("navigation_data.json")
categories = [(item["category"], item["subcategory"]) for item in test_data["categories"]]

@pytest.fixture
def page(context_no_ads):
    page = context_no_ads.new_page()
    yield page
    page.close()

@pytest.mark.parametrize("category, subcategory", categories)
def test_NA01_navigate_to_category(page, category, subcategory):
    products_page = ProductsPage (page)
    page.goto("/products")
    products_page.navigate_to_category(category, subcategory)
    breadcrumb_text = products_page.category_breadcrumb.inner_text()
    assert category in breadcrumb_text and subcategory in breadcrumb_text

#def test_NA02_navigate_to_brand():

#def test_NA03_navigate_to_product detail():


'''
| UI_NA01 | Navigate to Women > Dress category (parametrized for all 7 categories) | — | Category page should be displayed. Only products matching the selected category should be displayed |
| UI_NA02 | Navigate to a brand section (parametrized) | — | /brand_products/*brand* page should be displayed. Only products for the selected brand should be displayed |
| UI_NA03 | Navigate to a product detail | — | Product detail page is displayed |
'''
