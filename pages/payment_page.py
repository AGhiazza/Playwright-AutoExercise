from pages.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Payment Selectors

    @property
    def credit_card_name(self):
        return self.page.locator("[data-qa='name-on-card']")

    @property
    def credit_card_number(self):
        return self.page.locator("[data-qa='card-number']")

    @property
    def credit_card_cvc(self):
        return self.page.locator("[data-qa='cvc']")

    @property
    def credit_card_expiry_month(self):
        return self.page.locator("[data-qa='expiry-month']")

    @property
    def credit_card_expiry_year(self):
        return self.page.locator("[data-qa='expiry-year']")

    @property
    def pay_and_confirm_button(self):
        return self.page.locator("#submit")

    ##Payment Confirmation Selectors

    @property
    def order_placed_message(self):
        return self.page.locator("[data-qa='order-placed']")

    @property
    def download_invoice_button(self):
        return self.page.locator("a[href*='/download_invoice/']")

    ##Payment Methods

    def fill_payment_details(self, name, card_number, cvc, month, year):
        self.credit_card_name.fill(name)
        self.credit_card_number.fill(card_number)
        self.credit_card_cvc.fill(cvc)
        self.credit_card_expiry_month.fill(month)
        self.credit_card_expiry_year.fill(year)
        self.pay_and_confirm_button.click()
