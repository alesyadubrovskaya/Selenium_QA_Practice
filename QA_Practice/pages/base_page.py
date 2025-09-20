class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open_page(self, URL):
        self.browser.get(URL)

    def find_elem(self, args):
        return self.browser.find_element(*args)