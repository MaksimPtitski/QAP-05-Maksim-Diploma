from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        raise NotImplementedError

    def open_home_page(self):
        self.driver.get("https://www.ourgroceries.com/sign-in?url=%2Fyour-lists%2F")

    def find_element(self, *args):
        by, val = args[0]
        return self.driver.find_element(by, val)

    def is_element_displayed(self, element):
        self.find_element(element).is_displayed()
