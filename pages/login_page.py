from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Login Selectors
    @property
    def login_email(self):
        return self.page.locator("[data-qa='login-email']")
    
    @property
    def login_password(self):
        return self.page.locator("[data-qa='login-password']")

    @property
    def login_button(self):
        return self.page.locator("[data-qa='login-button']")

    @property
    def login_error_message(self):
        return self.page.locator(".login-form p")

    ##Signup Selectors

    @property
    def signup_name(self):
        return self.page.locator("[data-qa='signup-name']")
    
    @property
    def signup_email(self):
        return self.page.locator("[data-qa='signup-email']")

    @property
    def signup_button(self):
        return self.page.locator("[data-qa='signup-button']")

    @property
    def signup_error_message(self):
        return self.page.locator(".signup-form p")

    #Login Methods

    def login(self, user, password):
        self.login_email.fill(user)
        self.login_password.fill(password)
        self.login_button.click()

    def get_login_error_message(self):
        return self.login_error_message.inner_text()
    
    #Signup Methods

    def signup(self, name, email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()

    def get_signup_error_message(self):
        return self.signup_error_message.inner_text()