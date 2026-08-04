class BasePage:
    def __init__(self, page):

        self.page = page

    #Selectors

    ##Header Selectors

    @property
    def nav_home_link(self):
        return self.page.locator(".nav.navbar-nav a[href='/']")
    
    @property
    def nav_products_link(self):
        return self.page.locator("a[href='/products']")

    @property
    def nav_cart_link(self):
        return self.page.locator(".nav.navbar-nav a[href='/view_cart']")

    @property
    def nav_login_link(self):
        return self.page.locator("a[href='/login']")

    @property
    def nav_contact_link(self):
        return self.page.locator("a[href='/contact_us']")

    @property
    def logout_button(self):
        return self.page.locator("a[href='/logout']")

    @property
    def delete_account_button(self):
        return self.page.locator("a[href='/delete_account']")

    @property
    def logged_username(self):  #"Logged in as *****"
        return self.page.locator(".nav.navbar-nav a b")

    ##HomePage Selectors

    @property
    def first_product_name(self):
        return self.page.locator(".productinfo p").first

    @property
    def first_product_add_to_cart_button(self):
        return self.page.locator(".add-to-cart").first

    @property
    def first_view_product_link(self):
        return self.page.locator("a[href*='/product_details/']").first

    @property
    def view_cart_button(self):
        return self.page.locator("#cartModal a[href='/view_cart']")

    @property
    def continue_shopping_button(self):
        return self.page.locator(".close-modal")

    @property
    def account_deleted_message(self): #Message displayed when an account is deleted in the /delete_account URL, it's here since there is no point in creating a class exclusively for it (DeletePage)
        return self.page.locator("[data-qa='account-deleted']")
    
    ##Footer Selectors
    
    @property
    def subscription_email_input(self):
        return self.page.locator("#susbscribe_email")
    
    @property
    def subscription_submit_button(self):
        return self.page.locator("#subscribe")
    
    @property
    def subscription_success_message(self):
        return self.page.locator("#success-subscribe")

    #Methods

    ##Header Navigation Methods

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

    def get_logged_in_username (self): #Gets the username in the header that is currently logged in
        return self.logged_username.inner_text()

    ##Ad Methods

    def dismiss_ad(self): #Ad dismissal method necesary for the proper navigation during tests
        try:
            self.page.wait_for_selector("#dismiss-button", timeout=3000)
            self.page.locator("#dismiss-button").click()
        except:
            pass

    ##Sidebar Methods

    def navigate_to_category(self, category, subcategory):
        self.dismiss_ad()   #Have to call the close ad twice (before clicking the category and after) because of its random nature
        self.page.locator(f"a[href='#{category}']").click()
        self.dismiss_ad()
        self.page.locator(f"#{category} a:has-text('{subcategory}')").wait_for(state="visible")
        self.page.locator(f"#{category} a:has-text('{subcategory}')").click()

    def click_on_brand(self, brand):
        self.page.locator(f".brands-name a:has-text('{brand}')").click()
        
    ##Footer Subscription Methods

    def subscribe (self, email):
        self.subscription_email_input.fill(email)
        self.subscription_submit_button.click()