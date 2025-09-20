def test_valid_regist_submit():
    driver.find_element(By.CSS_SELECTOR, "#firstName").send_keys('admin12admin.com')
    driver.find_element(By.CSS_SELECTOR, "#lastName").send_keys('a')
    driver.find_element(By.CSS_SELECTOR, "#phone").send_keys('admin12admin.com')
    driver.find_element(By.CSS_SELECTOR, "#countries_dropdown_menu").click()
    driver.find_element(By.CSS_SELECTOR, "#emailAddress").send_keys('admin12admin.com')
    driver.find_element(By.CSS_SELECTOR, "#emailAddress").send_keys('admin12admin.com')
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys('a')
    driver.find_element(By.CSS_SELECTOR, ".form-check-input").send_keys('a')
    driver.find_element(By.CSS_SELECTOR, "#registerBtn").click()
    alert_mw = driver.find_element(By.CSS_SELECTOR, ".alert-danger").is_displayed()
    alert = driver.find_element(By.CSS_SELECTOR, ".alert-danger").text
    alert_color = driver.find_element(By.CSS_SELECTOR, ".alert-danger").value_of_css_property("background-color")
    alert_font = driver.find_element(By.CSS_SELECTOR, ".alert-danger").value_of_css_property("font-size")
    print(alert_color, alert_font)
    assert alert_mw == True
    assert alert == "Bad credentials! Please try again! Make sure that you've registered."
    time.sleep(5)
    driver.quit()