from selenium.webdriver.common.by import By
from browser import Browser


class BasePage(Browser):
    # Base Page Locators

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.browser.title





