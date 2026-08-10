import pytest
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from utils.logger import logger
from utils.data_reader import read_json

test_data = read_json("user_data.json")
user_data = test_data["register_user_data"]

@pytest.mark.ui
@pytest.mark.parametrize("testpage", ["/", "/products"])
def test_CA01_add_product_to_cart_then_login(page, testpage, registered_user):
    products_page = ProductsPage(page)
    cart_page = CartPage(page)
    login_page = LoginPage(page)
    logger.info(f"Navigating to {testpage}")
    page.goto(testpage)
    first_product = products_page.first_product_name.inner_text()
    logger.info("Adding first product to cart")
    products_page.first_product_add_to_cart_button.click()
    logger.info("Navigating to cart")
    products_page.view_cart_button.click()
    logger.info("Clicking on Checkout")
    cart_page.checkout_button.click()
    logger.info("Login in")
    cart_page.checkout_login_link.click()
    login_page.login(user_data["email"], user_data["password"])
    cart_page.navigate_to_cart()
    logger.info("Verifying logged user retains cart items")
    assert cart_page.first_product_name.inner_text() == first_product
    logger.info("Logged user retained cart items successfully")

@pytest.mark.ui
def test_CA02_add_product_to_cart_from_recommended_items(page):
    home_page = HomePage(page)
    cart_page = CartPage(page)
    logger.info("Navigating to homepage")
    page.goto("/")
    logger.info("Adding first recommended product to cart")
    home_page.first_recommended_add_to_cart_button.click()
    cart_page.view_cart_button.click()
    logger.info("Verifying cart is not empty")
    assert not cart_page.empty_cart.is_visible()
    logger.info("Successful confirmation that cart is not empty")

@pytest.mark.ui
def test_CA03_add_same_product_multiple_times(page):
    cart_page = CartPage(page)
    logger.info("Navigating to Products")
    page.goto("/products")
    logger.info("Adding first product to cart")
    cart_page.first_product_add_to_cart_button.click()
    cart_page.continue_shopping_button.click()
    logger.info("Adding second product to cart")
    cart_page.first_product_add_to_cart_button.click()
    logger.info("Navigating to cart")
    cart_page.view_cart_button.click()
    logger.info("Verifying amount of items in cart")
    assert cart_page.product_quantity.inner_text() == "2"
    logger.info("Successful verification of item amount in cart")

@pytest.mark.ui
def test_CA04_add_product_with_quantity_from_product_detail(page):
    productdetail_page = ProductDetailPage(page)
    cart_page = CartPage(page)
    logger.info("Navigating to homepage")
    page.goto("/")
    logger.info("Navigating to first product's detail page")
    cart_page.first_view_product_link.click()
    logger.info("Adding multiple amount of the same product to cart")
    productdetail_page.quantity_input.fill("2")
    productdetail_page.add_to_cart_button.click()
    logger.info("Navigating to cart")
    cart_page.view_cart_button.click()
    logger.info("Verifying amount of items in cart")
    assert cart_page.product_quantity.inner_text() == "2"
    logger.info("Successful verification of item amount in cart")

@pytest.mark.ui
def test_CA05_remove_product_from_cart(page):
    cart_page = CartPage(page)
    logger.info("Navigating to homepage")
    page.goto("/")
    logger.info("Adding first product to cart")
    cart_page.first_product_add_to_cart_button.click()
    logger.info("Navigating to cart")
    cart_page.view_cart_button.click()
    logger.info("Removing product from cart")
    cart_page.first_delete_button.click()
    logger.info("Verifying Empty Cart page is displayed")
    cart_page.empty_cart.wait_for(state="visible")
    assert cart_page.empty_cart.is_visible()
    logger.info("Successful verification of Empty Cart page")

@pytest.mark.ui
def test_CA06_verify_empty_cart(page):
    cart_page = CartPage(page)
    logger.info("Navigating to cart")
    page.goto("/view_cart")
    logger.info("Verifying Empty Cart page is displayed")
    assert cart_page.empty_cart.is_visible()
    logger.info("Successful verification of Empty Cart page")