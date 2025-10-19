from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

URL = 'https://qa-practice.netlify.app/register'

fname_field = (By.CSS_SELECTOR, "#firstName")
lname_field = (By.CSS_SELECTOR, "#lastName")
phone_field = (By.CSS_SELECTOR, "#phone")
country_dropdown = (By.CSS_SELECTOR, "#countries_dropdown_menu")
email_field = (By.CSS_SELECTOR, "#emailAddress")
pass_field = (By.CSS_SELECTOR, "#password")
checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
submit_btn = (By.CSS_SELECTOR, "#registerBtn")
alert_success = (By.CSS_SELECTOR, ".alert-danger")


class SignUpPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_signup_page(self):
        self.open_page(URL)

    def enter_fname(self, fname):
        self.find_elem(fname_field).send_keys(fname)

    def enter_lname(self, lname):
        self.find_elem(lname_field).send_keys(lname)

    def enter_phone(self, phone):
        self.find_elem(phone_field).send_keys(phone)

    def choose_country(self, value):
        country_select = Select(self.find_elem(country_dropdown))
        country_select.select_by_value(value)

    def enter_email(self, email):
        self.find_elem(email_field).send_keys(email)

    def enter_password(self, password):
        self.find_elem(email_field).send_keys(password)

    def checkbox_clk(self):
        self.find_elem(checkbox).click()

    def submit(self):
        self.find_elem(submit_btn).click()

    @property
    def alert_success_is_displayed(self):
        return self.find_elem(alert_success).is_displayed()

    @property
    def alert_success_text(self):
        return self.find_elem(alert_success).text



