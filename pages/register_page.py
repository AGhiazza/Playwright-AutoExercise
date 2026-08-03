from pages.base_page import BasePage

class RegisterPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Register Selectors

    @property
    def create_account_button(self):
        return self.page.locator("[data-qa='create-account']")

    ##Account Information Selectors
    @property
    def acc_title_mr(self):
        return self.page.locator("#id_gender1")
    
    @property
    def acc_title_mrs(self):
        return self.page.locator("#id_gender2")
    
    @property
    def acc_name(self):
        return self.page.locator("[data-qa='name']")

    @property
    def acc_email(self):
        return self.page.locator("[data-qa='email']")
    
    @property
    def acc_password(self):
        return self.page.locator("[data-qa='password']")

    ##Address Information Selectors

    @property
    def address_info_name(self):
        return self.page.locator("[data-qa='first_name']")
    
    @property
    def address_info_lastname(self):
        return self.page.locator("[data-qa='last_name']")
    
    @property
    def address_info_address(self):
        return self.page.locator("[data-qa='address']")
    
    @property
    def address_info_country(self):
        return self.page.locator("[data-qa='country']")
    
    @property
    def address_info_state(self):
        return self.page.locator("[data-qa='state']")
    
    @property
    def address_info_city(self):
        return self.page.locator("[data-qa='city']")
    
    @property
    def address_info_zipcode(self):
        return self.page.locator("[data-qa='zipcode']")
    
    @property
    def address_info_mobile_number(self):
        return self.page.locator("[data-qa='mobile_number']")
    
    ##Account Created Selectors

    @property
    def account_created_message(self):
        return self.page.locator("[data-qa='account-created']")

    @property
    def account_created_continue_button(self):
        return self.page.locator("[data-qa='continue-button']")

    #Methods

    ##Account Information Methods

    def fill_account_info(self, password, name=None, email=None):
        if name:
            self.acc_name.fill(name)
        if email:
            self.acc_email.fill(email)
        self.acc_password.fill(password)

    ##Address Information Methods

    def fill_address_info(self, name, lastname, address, country, state, city, zipcode, mobile):
        self.address_info_name.fill(name)
        self.address_info_lastname.fill(lastname)
        self.address_info_address.fill(address)
        self.address_info_country.select_option(country)
        self.address_info_state.fill(state)
        self.address_info_city.fill(city)
        self.address_info_zipcode.fill(zipcode)
        self.address_info_mobile_number.fill(mobile)

    def click_on_create_account(self):
        self.create_account_button.click()