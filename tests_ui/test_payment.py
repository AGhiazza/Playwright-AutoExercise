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
