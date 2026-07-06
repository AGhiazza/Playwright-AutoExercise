from pages.base_page import BasePage

def test_smoke_navigation(page):
    base = BasePage(page)
    page.goto("https://automationexercise.com")
    base.navigate_to_products()
    assert "/products" in page.url