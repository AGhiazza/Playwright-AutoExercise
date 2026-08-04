from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Navigation Selectors
    @property
    def category_breadcrumb(self):
        return self.page.locator(".breadcrumb .active")

    ##Search Selectors

    @property
    def search_bar(self):
        return self.page.locator("#search_product")

    @property
    def search_button(self):
        return self.page.locator("#submit_search")

    ##Products Selectors

    @property
    def products_section_title(self):
        return self.page.locator(".title.text-center")

    @property
    def product_cards(self):
        return self.page.locator(".productinfo")

    #Methods
    
    ##Navigation Methods

    def click_on_first_view_product_details(self):
        self.first_view_product_link.click()

    def search_for_product(self, product):
        self.search_bar.fill(product)
        self.search_button.click()