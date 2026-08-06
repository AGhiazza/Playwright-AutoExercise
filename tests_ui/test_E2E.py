import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from pages.register_page import RegisterPage
from utils.data_reader import read_json

user_test_data = read_json("user_data.json")
user_data = user_test_data["register_user_data"]
payment_data = user_test_data["payment_data"]

nav_test_data = read_json("navigation_data.json")
valid_search_term = nav_test_data["valid_search_term"]

@pytest.mark.e2e
def test_E2E01_login_search_detail_add_checkout_payment_invoice(page, registered_user):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    productdetail_page = ProductDetailPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    products_page.navigate_to_products()
    products_page.search_for_product(valid_search_term)
    products_page.first_view_product_link.click()
    productdetail_page.quantity_input.fill("2")
    productdetail_page.add_to_cart_button.click()
    cart_page.view_cart_button.click()
    cart_page.checkout_button.click()
    checkout_page.place_order_button.click()
    payment_page.fill_payment_details(payment_data["card_name"], payment_data["card_number"], payment_data["card_cvc"], payment_data["card_month"], payment_data["card_year"])
    with page.expect_download() as download_info:
        payment_page.download_invoice_button.click()
    download = download_info.value
    download_path = download.path()
    with open(download_path, "r") as f:
        content = f.read()
    assert user_data["firstname"] in content

@pytest.mark.e2e
def test_E2E02_add_checkout_register_checkout_payment_delete(page):
    login_page = LoginPage(page)
    register_page = RegisterPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    page.goto("/")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    cart_page.checkout_button.click()
    cart_page.checkout_login_link.click()
    login_page.signup(user_data["name"], user_data["email"])
    register_page.fill_account_info(user_data["password"])
    register_page.fill_address_info(user_data["firstname"], user_data["lastname"], user_data["address"], user_data["country"], user_data["state"], user_data["city"], user_data["zipcode"], user_data["mobile"])
    register_page.click_on_create_account()
    register_page.account_created_continue_button.click()
    cart_page.navigate_to_cart()
    cart_page.checkout_button.click()
    checkout_page.place_order_button.click()
    payment_page.fill_payment_details(payment_data["card_name"], payment_data["card_number"], payment_data["card_cvc"], payment_data["card_month"], payment_data["card_year"])
    with page.expect_download() as download_info:
        payment_page.download_invoice_button.click()
    download = download_info.value
    download_path = download.path()
    with open(download_path, "r") as f:
        content = f.read()
    assert user_data["firstname"] in content
    login_page.click_on_delete_account ()
    assert login_page.account_deleted_message.is_visible()