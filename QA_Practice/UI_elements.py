import time
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

url_form = driver.get('https://qa-practice.netlify.app/auth_ecommerce')
def test_valid_form_submit():
    driver.find_element(By.CSS_SELECTOR, "#email").send_keys('admin@admin.com')
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys('admin123')
    driver.find_element(By.CSS_SELECTOR, "#submitLoginBtn").click()
    time.sleep(5)
    driver.quit()

