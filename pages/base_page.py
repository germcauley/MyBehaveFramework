
from browser import Browser
from selenium.webdriver.common.by import By
import time

class BasePage(Browser):

    def navigate(self, address):
        self.driver.get(address)

    def refresh(self):
        self.driver.refresh()

    def cookie_click(self):
        COOKIE_BUTTON = self.driver.find_element(By.CSS_SELECTOR,'button.optanon-allow-all')
        COOKIE_BUTTON.click()
        time.sleep(2)