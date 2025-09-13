import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url_form = driver.get('https://qa-practice.netlify.app/dropdowns')

def test_dropdown1_1():
    select_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-menu'))
    select_dropdown.select_by_value('Belarus')
    select_dropdown.select_by_value('Japan')
    time.sleep(3)
    driver.quit()


def test_dropdown1_2():
    select_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-menu'))
    ls = []
    for opt in select_dropdown.options:
        select_dropdown.select_by_visible_text(opt.get_attribute("text"))
        ls.append(opt.get_attribute('text'))
    print('\n'.join(ls))
    time.sleep(3)
    driver.quit()


def test_dropdown2_1():
    dropdown_btn = driver.find_element(By.CSS_SELECTOR, '#multi-level-dropdown-btn').click()
    option3 = driver.find_element(By.XPATH, "//a[text() = 'Hover me for more options']")
    sub_opt2 = driver.find_element(By.XPATH, "//a[@href='#hover-me']")
    sub_opt3 = driver.find_element(By.XPATH, "//a[text() = 'Even More..']")
    sub_opt4 = driver.find_element(By.XPATH, "//a[text() = 'another level']")
    final4_2 = driver.find_element(By.XPATH, "//a[text() = '4th level - 2']")
    actions = ActionChains(driver)
    actions.move_to_element(option3).perform()
    actions.move_to_element(sub_opt2).perform()
    actions.move_to_element(sub_opt3).perform()
    actions.move_to_element(sub_opt4).perform()
    final4_2.click()
    time.sleep(3)
    driver.quit()


def test_dropdown2_2():
    dropdown_btn = driver.find_element(By.CSS_SELECTOR, '#multi-level-dropdown-btn').click()
    option3 = driver.find_element(By.XPATH, "//a[text() = 'Hover me for more options']")
    sub_opt2 = driver.find_element(By.XPATH, "//a[@href='#hover-me']")
    sub_opt3 = driver.find_element(By.XPATH, "//a[text() = 'Even More..']")
    lev3_1opt = driver.find_element(By.XPATH, "//a[text()='3rd level - 1']")
    actions = ActionChains(driver)
    actions.move_to_element(option3).perform()
    actions.move_to_element(sub_opt2).perform()
    actions.move_to_element(sub_opt3).perform()
    lev3_1opt.click()
    time.sleep(3)
    driver.quit()