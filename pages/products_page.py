from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Navigation Selectors
    @property
    def category_breadcrumb (self):
        return self.page.locator(".breadcrumb .active")