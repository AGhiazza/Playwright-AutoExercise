import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]

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