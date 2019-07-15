from selenium.webdriver.common.by import By
from selenium import webdriver


class BasePage(object):
    # Base Page Locators
    def __init__(context):
        # context.base_url = base_url
        context.driver = webdriver.Chrome()
        context.timeout = 30
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(30)
        context.driver.maximize_window()

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.get()


