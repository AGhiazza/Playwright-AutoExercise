import pytest

@pytest.mark.api
def test_PL01_get_all_products(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.get("/api/productsList")
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    api.dispose()

@pytest.mark.api
def test_PL02_post_to_all_products_list(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/productsList", data={})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 405
    api.dispose()
