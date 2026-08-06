from pages.base_page import BasePage

def test_smoke_navigation(page):
    base = BasePage(page)
    page.goto("/")
    base.navigate_to_products()
    assert "/products" in page.url