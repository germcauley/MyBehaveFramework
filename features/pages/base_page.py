from selenium.webdriver.common.by import By
from browser import Browser


class BasePage(Browser):
    # Base Page Locators

    def navigate(self, address):
        self.driver.get(address)



    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "search")
    SUBMIT_BUTTON = (By.CLASS_NAME, "search-form__button")

