from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Product Details Selectors

    @property
    def product_name(self):
        return self.page.locator(".product-information h2")
    
