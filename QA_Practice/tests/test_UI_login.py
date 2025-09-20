from pages.login_page import LoginPage
import time


def test_valid_login_submit(browser):
    login_page = LoginPage(browser)
    login_page.login_page_open()
    login_page.enter_email('admin@admin.com')
    login_page.enter_psw('admin123')
    login_page.press_submit()
    assert login_page.shop_is_displayed == True
    time.sleep(5)


def test_invalid_login_submit(browser):
    login_page = LoginPage(browser)
    login_page.login_page_open()
    login_page.enter_email('admin12admin.com')
    login_page.enter_psw('a')
    login_page.press_submit()
    assert login_page.shop_is_displayed == False
    assert login_page.alert_is_dislpayed == True
    assert login_page.alert_txt == "Bad credentials! Please try again! Make sure that you've registered."
    login_page.alert_attributes()
    time.sleep(5)




