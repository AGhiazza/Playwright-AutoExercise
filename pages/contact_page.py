from pages.base_page import BasePage

class ContactPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    #Selectors

    ##Contact Selectors

    @property
    def contact_name(self):
        return self.page.locator("[data-qa='name']")

    @property
    def contact_email(self):
        return self.page.locator("[data-qa='email']")

    @property
    def contact_subject(self):
        return self.page.locator("[data-qa='subject']")

    @property
    def contact_message(self):
        return self.page.locator("[data-qa='message']")

    @property
    def contact_sumbit_button(self):
        return self.page.locator("[data-qa='submit-button']")

    @property
    def contact_success_message(self):
        return self.page.locator(".status.alert-success")

    ##Contact Methods

    def fill_contact_message(self, name, email, subject, message):
            self.contact_name.fill(name)
            self.contact_email.fill(email)
            self.contact_subject.fill(subject)
            self.contact_message.fill(message)
            self.contact_sumbit_button.click()
