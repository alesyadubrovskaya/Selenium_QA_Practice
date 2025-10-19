import time
from pages.dropdowns_page import DropdownPage


def test_dropdown1_1(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.open_dropdown_page()
    assert dropdown_page.orig_val_is_displayed == True
    dropdown_page.choose_dropdown1_opt_val('Japan')
    assert dropdown_page.chosen_val_txt == True
    time.sleep(5)


def test_dropdown1_2(browser):
    dropdown_page = DropdownPage(browser)
    dropdown_page.open_dropdown_page()
    assert dropdown_page.orig_val_is_displayed == True
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