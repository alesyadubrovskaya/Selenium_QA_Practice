from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import random

URL = 'https://qa-practice.netlify.app/dropdowns'

dropdown1 = (By.CSS_SELECTOR, '#dropdown-menu')
dropdown1_orig_opt = (By.XPATH, "//option[text()='Select a country...']")
dropdown1_opt = (By.XPATH, "//option[@value]")

dropdown2_btn = (By.CSS_SELECTOR, '#multi-level-dropdown-btn')
dropdown2_1 = (By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[1]")
dropdown2_1_subopt = (By.XPATH, "//a[text() = 'Hover me for more options']")
dropdown2_2 = (By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[2]")
dropdown2_2_subopt = (By.XPATH, "//a[text() = 'Even More..']")
dropdown2_3 = (By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[3]")
dropdown2_3_subopt = (By.XPATH, "//a[text() = 'another level']")
dropdown2_4 = (By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[4]")
dropdown2_4_final = (By.XPATH, "//a[text() = '4th level - 2']")
dropdown2_3_first = (By.XPATH, "//a[text()='3rd level - 1']")

class DropdownPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open_dropdown_page(self):
        self.open_page(URL)

    def choose_dropdown1_opt_val(self, value):
        country_dd = Select(self.find_elem(dropdown1))
        country_dd.select_by_value(value)

    def choose_dropdown1_random_opt(self, values):
        country_dd = Select(self.find_elem(dropdown1))

        country_dd.select_by_visible_text(random.choice(values))

    @property
    def orig_val_is_displayed(self):
        return self.find_elem(dropdown1_orig_opt).is_displayed()

    @property
    def chosen_val_txt(self):
        return self.find_elem(dropdown1_opt).text

    def open_dropdown2(self):
        self.find_elem(dropdown2_1).click()

    def hover_subopt2_1(self, browser):
        actions = ActionChains(browser)
        actions.move_to_element(self.find_elem(dropdown2_1_subopt)).perform()

    def hover_subopt2_2(self, browser):
        actions = ActionChains(browser)
        actions.move_to_element(self.find_elem(dropdown2_2_subopt)).perform()

    def hover_subopt2_3(self, browser):
        actions = ActionChains(browser)
        actions.move_to_element(self.find_elem(dropdown2_3_subopt)).perform()

