from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from hamcrest import *
import time

class BBPAGE(BasePage):

    # def navigate(self, address):
    #     self.driver.get(address)
    #     time.sleep(5)

    # def cookie_click(self):
    #     COOKIE_BUTTON = self.driver.find_element(By.CSS_SELECTOR,'button.optanon-allow-all')
    #     COOKIE_BUTTON.click()
    #     time.sleep(2)

    def search_bca(self, search_term):
        SEARCH_BAR = self.driver.find_element(By.CSS_SELECTOR,'.c-mm-condensed__search-form-input')
        SEARCH_BAR.send_keys('Business Current Account')
        SEARCH_BAR.send_keys(Keys.ENTER)
        time.sleep(2)



