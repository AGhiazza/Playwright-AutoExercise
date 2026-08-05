from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Address Details Selectors

    @property
    def delivery_firstname_lastname(self):
        return self.page.locator("#address_delivery .address_firstname.address_lastname")

    @property
    def delivery_address(self):
        return self.page.locator("#address_delivery .address_address1.address_address2:not(:empty)")

    @property
    def delivery_country(self):
        return self.page.locator("#address_delivery .address_country_name")
    
    ##Review Your Order Selectors

    @property
    def cart_total_price(self):
        return self.page.locator("tr:has-text('Total Amount') .cart_total_price")

    @property
    def place_order_button(self):
        return self.page.locator("a[href='/payment']")