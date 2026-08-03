from pages.base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Product Details Selectors

    @property
    def product_name(self):
        return self.page.locator(".product-information h2")
    
    ##Review Selectors

    @property
    def review_name(self):
        return self.page.locator("#name")
    
    @property
    def review_email(self):
        return self.page.locator("#email")
    
    @property
    def review_textbox(self):
        return self.page.locator("#review")
    
    @property
    def submit_review_button(self):
        return self.page.locator("#button-review")
    
    @property
    def successful_review_submission_message(self):
        return self.page.locator("#review-section .alert-success")

    #Methods

    ##Review Methods

    def write_a_review(self, name, email, review):
        self.review_name.fill(name)
        self.review_email.fill(email)
        self.review_textbox.fill(review)
        self.submit_review_button.click()