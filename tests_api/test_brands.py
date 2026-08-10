import pytest
from utils.logger import logger

@pytest.mark.api
def test_BR01_get_all_brands(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.get("/api/brandsList")

    print(response.status)
    print(response.json())

    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    api.dispose()

@pytest.mark.api
def test_BR02_post_to_all_brands(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/brandsList", data={})

    print(response.status)
    print(response.json())

    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 405
    api.dispose()
