import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]

@pytest.mark.ui
def test_CH01_attempt_checkout_with_no_signin(page):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    page.goto("/")
    products_page.first_product_add_to_cart_button.click()
    products_page.view_cart_button.click()
    cart_page.checkout_button.click()
    assert cart_page.checkout_login_modal.is_visible()

@pytest.mark.ui
def test_CH02_verify_address_details_in_checkout(page, registered_user):
    registered_address = user_data["address"]
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    products_page.first_product_add_to_cart_button.click()
    products_page.view_cart_button.wait_for(state="visible")
    products_page.view_cart_button.click()
    cart_page.checkout_button.click()
    checkout_address = checkout_page.delivery_address.inner_text()
    assert checkout_address == registered_address

def test_CH03_verify_total_amount_in_checkout(page, registered_user):
    login_page = LoginPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    cart_page.first_product_add_to_cart_button.wait_for(state="visible")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.continue_shopping_button.click()
    cart_page.first_product_add_to_cart_button.wait_for(state="visible")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.wait_for(state="visible")
    cart_page.view_cart_button.click()
    product_price = cart_page.first_product_price.inner_text()
    cart_page.checkout_button.click()
    cart_total_price = checkout_page.cart_total_price.inner_text()
    price_number = int(product_price.replace("Rs. ", ""))
    assert cart_total_price == f"Rs. {price_number * 2}"
