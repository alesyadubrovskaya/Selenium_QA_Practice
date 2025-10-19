from pages.registry_page import SignUpPage
import time


def test_valid_register_submit(browser):
    signup = SignUpPage(browser)
    signup.open_signup_page()
    signup.enter_fname('Alex')
    signup.enter_lname('Flowers')
    signup.enter_phone('1234567890')
    signup.choose_country('Belarus')
    signup.enter_email('tussunnacozo-8928@yopmail.com')
    signup.enter_password('qwerty123')
    signup.checkbox_clk()
    signup.submit()
    assert signup.alert_success_is_displayed == True
    assert signup.alert_success_text == 'The account has been successfully created!'
    time.sleep(5)
