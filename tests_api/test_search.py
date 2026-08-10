import pytest
from utils.logger import logger

@pytest.mark.api
def test_SR01_search_valid_product(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/searchProduct", form={"search_product": "top"})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    api.dispose()

@pytest.mark.api
def test_SR02_search_blank_product(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/searchProduct")
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 400
    api.dispose()
