from pages.base_page import BasePage
from browser import Browser


class HomePage(BasePage):
    # Home Page Actions


    def get_page_title(self):
        return self.driver.title



