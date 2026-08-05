import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]
payment_data = test_data["payment_data"]

def test_PY01_complete_an_order(page, registered_user):
    login_page = LoginPage(page)        
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    cart_page.checkout_button.click()
    checkout_page.place_order_button.click()
    payment_page.fill_payment_details(payment_data["card_name"], payment_data["card_number"], payment_data["card_cvc"], payment_data["card_month"], payment_data["card_year"])
    assert payment_page.order_placed_message.is_visible()

def test_PY02_download_invoice_after_successful_order(page, registered_user):
    login_page = LoginPage(page)        
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)
    payment_page = PaymentPage(page)
    page.goto("/login")
    login_page.login(user_data["email"], user_data["password"])
    cart_page.first_product_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    first_product_price = cart_page.first_product_price.inner_text() #Saves product price
    price_number = first_product_price.replace("Rs. ", "") #Cleans currency symbol
    cart_page.checkout_button.click()
    checkout_page.place_order_button.click()
    payment_page.fill_payment_details(payment_data["card_name"], payment_data["card_number"], payment_data["card_cvc"], payment_data["card_month"], payment_data["card_year"])
    with page.expect_download() as download_info:
        payment_page.download_invoice_button.click()
    download = download_info.value
    download_path = download.path()
    with open(download_path, "r") as f:
        content = f.read()
    assert price_number in content 
    assert user_data["firstname"] in content
    assert "Thank you" in content
  
@pytest.mark.skip(reason="Browser-native validation, not application logic. Covered at API level.")
def test_PY03_attempt_payment_with_empty_field(page):
    pass