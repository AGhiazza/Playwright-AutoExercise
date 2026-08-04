from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Cart Selectors

    @property
    def product_description(self):
        return self.page.locator(".cart_description")

    @property
    def first_product_name(self):
        return self.page.locator(".cart_description h4 a").first

    @property
    def first_product_price(self):
        return self.page.locator(".cart_price").first

    @property
    def first_delete_button(self):
        return self.page.locator(".cart_quantity_delete").first

    @property
    def product_quantity(self):
        return self.page.locator(".cart_quantity button")

    ##Checkout Selectors

    @property
    def checkout_login_modal(self):
        return self.page.locator("#checkoutModal")

    @property
    def checkout_button(self):
        return self.page.locator(".check_out")

    @property
    def checkout_login_link(self):
        return self.page.locator("#checkoutModal a[href='/login']")

    ##Empty Cart Selectors

    @property
    def empty_cart(self):
        return self.page.locator("#empty_cart p")   

    