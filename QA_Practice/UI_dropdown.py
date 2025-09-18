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
driver.maximize_window()

url_form = driver.get('https://qa-practice.netlify.app/dropdowns')


def test_dropdown1_1():
    select_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-menu'))
    orig_opt = driver.find_element(By.XPATH, "//option[text()='Select a country...']")
    bel_opt = driver.find_element(By.XPATH, "//option[text()='Belarus']")
    jp_opt = driver.find_element(By.XPATH, "//option[text()='Japan']")
    assert orig_opt.is_selected() == True
    select_dropdown.select_by_value('Belarus')
    assert bel_opt.is_selected() == True
    select_dropdown.select_by_value('Japan')
    assert jp_opt.is_selected() == True
    time.sleep(3)
    driver.quit()


def test_dropdown1_2():
    select_dropdown = Select(driver.find_element(By.CSS_SELECTOR, '#dropdown-menu'))
    orig_opt = driver.find_element(By.XPATH, "//option[text()='Select a country...']")
    assert orig_opt.is_selected() == True
    ls = []
    for opt in select_dropdown.options:
        select_dropdown.select_by_visible_text(opt.get_attribute("text"))
        assert opt.is_selected() == True
        ls.append(opt.get_attribute('text'))
    print('\n'.join(ls))
    time.sleep(3)
    driver.quit()


def test_dropdown2_1():
    dropdown_btn = driver.find_element(By.CSS_SELECTOR, '#multi-level-dropdown-btn')
    dropdown_btn.click()
    dr1 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[1]")
    assert dr1.is_displayed() == True
    option3 = driver.find_element(By.XPATH, "//a[text() = 'Hover me for more options']")
    dr2 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[2]")
    sub_opt3 = driver.find_element(By.XPATH, "//a[text() = 'Even More..']")
    dr3 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[3]")
    sub_opt4 = driver.find_element(By.XPATH, "//a[text() = 'another level']")
    dr4 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[4]")
    final4_2 = driver.find_element(By.XPATH, "//a[text() = '4th level - 2']")
    actions = ActionChains(driver)
    actions.move_to_element(option3).perform()
    assert dr2.is_displayed() == True
    actions.move_to_element(sub_opt3).perform()
    assert dr3.is_displayed() == True
    actions.move_to_element(sub_opt4).perform()
    assert dr4.is_displayed() == True
    final4_2.click()
    time.sleep(3)
    driver.quit()


def test_dropdown2_2():
    dropdown_btn = (driver.find_element(By.CSS_SELECTOR, '#multi-level-dropdown-btn'))
    dropdown_btn.click()
    dr1 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[1]")
    assert dr1.is_displayed() == True
    option3 = driver.find_element(By.XPATH, "//a[text() = 'Hover me for more options']")
    dr2 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[2]")
    dr3 = driver.find_element(By.XPATH, "(//ul[contains(@class, 'dropdown-menu')])[3]")
    sub_opt3 = driver.find_element(By.XPATH, "//a[text() = 'Even More..']")
    lev3_1opt = driver.find_element(By.XPATH, "//a[text()='3rd level - 1']")
    actions = ActionChains(driver)
    actions.move_to_element(option3).perform()
    assert dr2.is_displayed() == True
    actions.move_to_element(sub_opt3).perform()
    assert dr3.is_displayed() == True
    lev3_1opt.click()
    time.sleep(3)
    driver.quit()