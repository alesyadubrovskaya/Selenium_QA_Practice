from pages.base_page import BasePage
from selenium.webdriver.common.by import By

URL = 'https://qa-practice.netlify.app/auth_ecommerce'

email_field = (By.CSS_SELECTOR, "#email")
pass_field = (By.CSS_SELECTOR, "#password")
submit_btn = (By.CSS_SELECTOR, "#submitLoginBtn")
shop_UI = (By.CSS_SELECTOR, "#prooood")
alert_mw = (By.CSS_SELECTOR, ".alert-danger")

class LoginPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def login_page_open(self):
        self.open_page(URL)

    def enter_email(self, email):
        return self.find_elem(email_field).send_keys(email)

    def enter_psw(self, psw):
        return self.find_elem(pass_field).send_keys(psw)

    def press_submit(self):
        return self.find_elem(submit_btn).click()

    @property
    def shop_is_displayed(self):
        return self.find_elem(shop_UI).is_displayed()

    @property
    def alert_is_dislpayed(self):
        return self.find_elem(alert_mw).is_displayed()

    @property
    def alert_txt(self):
        return self.find_elem(alert_mw).text

    def alert_attributes(self):
        bg_color = self.find_elem(alert_mw).value_of_css_property("background-color")
        font_size = self.find_elem(alert_mw).value_of_css_property("font-size")
        print(bg_color, font_size)