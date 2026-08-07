def test_API_BR01_get_all_brands(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.get("/api/brandsList")
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 200
    api.dispose()

def test_API_BR02_post_to_all_brands(playwright, base_url):
    api = playwright.request.new_context(base_url=base_url)
    response = api.post("/api/brandsList", data={})
    assert response.status == 200
    response_json = response.json()
    assert response_json["responseCode"] == 405
    api.dispose()
