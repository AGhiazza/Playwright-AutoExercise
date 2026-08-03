from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Recommended Items Selectors

    @property
    def first_recommended_add_to_cart(self):
        return self.page.locator("#recommended-item-carousel .add-to-cart").first