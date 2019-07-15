from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage(object):
    # Base Page Locators
    def __init__(self):
        # self.base_url = base_url
        self.driver = webdriver.Chrome()
        self.timeout = 30
        self.driver.implicitly_wait(30)
        self.driver.set_page_load_timeout(30)
        self.driver.maximize_window()

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.get()


