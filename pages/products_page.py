from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Navigation Selectors
    @property
    def category_breadcrumb (self):
        return self.page.locator(".breadcrumb .active")

    @property
    def first_view_product_link(self):
        return self.page.locator("a[href*='/product_details/']").first
    

    # Navigation Methods

    def click_on_first_view_product_details(self):
        self.first_view_product_link.click()