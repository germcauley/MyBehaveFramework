from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage(object):
    # Base Page Locators
    def __init__(self,context):
        # self.base_url = base_url
        self.context = context
        self.driver = webdriver.Chrome()

        self.timeout = 30
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def close(self):
        self.driver.get()


