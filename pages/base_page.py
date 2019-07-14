
from browser import Browser
from selenium.webdriver.common.by import By
import time

class BasePage(object):

    def __init__(self, context):
        self.context = context
        self.driver = context.driver
        self.timeout = 30

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def cookie_click(self):
        COOKIE_BUTTON = self.driver.find_element(By.CSS_SELECTOR,'button.optanon-allow-all')
        COOKIE_BUTTON.click()
        time.sleep(2)