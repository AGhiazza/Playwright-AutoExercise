class BasePage:
    def __init__(self, page):

        self.page = page

    #Selectors

    @property
    def nav_home_link(self):
        return self.page.locator()
    
    @property
    def nav_products_link(self):
        return self.page.locator()

    @property
    def nav_cart_link(self):
        return self.page.locator()

    @property
    def nav_login_link(self):
        return self.page.locator()

    @property
    def nav_contact_link(self):
        return self.page.locator()

    @property
    def logout_button(self):
        return self.page.locator()

    @property
    def delete_account_button(self):
        return self.page.locator()
    
    @property
    def logged_username(self):
        return self.page.locator()
    
    @property
    def subscription_email_input(self):
        return self.page.locator()
    
    @property
    def subscription_submit_button(self):
        return self.page.locator()


    # Header Navigation Methods

    def navigate_to_home (self):
        self.nav_home_link.click()

    def navigate_to_products(self):
        self.nav_products_link.click()

    def navigate_to_cart (self):
        self.nav_cart_link.click()

    def navigate_to_login (self):
        self.nav_login_link.click()

    def navigate_to_contact (self):
        self.nav_contact_link.click()

    def click_on_logout (self):
        self.logout_button.click()
    
    def click_on_delete_account (self):
        self.delete_account_button.click()

    def get_logged_in_username (self, user): #Gets the username in the header that is currently logged in
        return self.logged_username.inner_text()

    # Sidebar Methods

    def navigate_to_category(self, category, subcategory):


    def click_on_brand(self, brand):

        
    # Footer Subscription Methods

    def subscribe (self, email):
        self.subscription_email_input.fill(email)
        self.subscription_submit_button.click()