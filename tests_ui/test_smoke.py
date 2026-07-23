from pages.base_page import BasePage
from utils.data_reader import read_json

config = read_json("config.json")
base_url = config["base_url"]

def test_smoke_navigation(page):
    base = BasePage(page)
    page.goto(base_url)
    base.navigate_to_products()
    assert "/products" in page.url