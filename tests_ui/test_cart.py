import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]
'''
@pytest.mark.parametrize("testpage", ["/", "/products"])
def test_CA01_add_product_to_cart_then_login(page, testpage, registered_user):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)
    page.goto(testpage)
    first_product = products_page.first_product_name.inner_text()
    products_page.first_product_add_to_cart_button.click()
    products_page.view_cart_button.click()
    cart_page.checkout_button.click()
    cart_page.checkout_login_link.click()
    login_page.login(user_data["email"], user_data["password"])
    cart_page.navigate_to_cart()
    assert cart_page.first_product_name.inner_text() == first_product

def test_CA02_add_product_to_cart_from_recommended_items(page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    page.goto("/")
    home_page.first_recommended_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    assert not cart_page.empty_cart.is_visible()

def test_CA03_add_same_product_multiple_times(page):
    cart_page = CartPage(page)
    page.goto("/products")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.continue_shopping_button.click()
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    assert cart_page.product_quantity.inner_text() == "2"

def test_CA04_add_product_with_quantity_from_product_detail(page):
    productdetail_page = ProductDetailPage(page)
    cart_page = CartPage(page)
    page.goto("/")
    cart_page.first_view_product_link.click()
    productdetail_page.quantity_input.fill("2")
    productdetail_page.add_to_cart_button.click()
    cart_page.view_cart_button.click()
    assert cart_page.product_quantity.inner_text() == "2"
'''
def test_CA05_remove_product_from_cart(page):
    cart_page = CartPage(page)
    page.goto("/")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    cart_page.first_delete_button.click()
    cart_page.empty_cart.wait_for(state="visible")
    assert cart_page.empty_cart.is_visible()