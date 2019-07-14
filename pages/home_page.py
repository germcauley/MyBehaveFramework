from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from hamcrest import *
import time

class HomePage(BasePage):

    def __init__(self):
        BasePage.__init__(self)

    def click_cookie(self):
        COOKIE_BUTTON = self.driver.find_element(By.CSS_SELECTOR,"button.optanon-allow-all")
        COOKIE_BUTTON.click()

    # def navigate(self, address):
    #     self.driver.get(address)
    #     time.sleep(5)

    def get_page_title(self):
        return self.driver.title

    def search(self, search_term):
        SEARCH_FIELD = self.driver.find_element(By.CSS_SELECTOR, "#cludo_search_form_mm_condensed > input")
        SEARCH_FIELD.send_keys('Cards')
        SEARCH_FIELD.send_keys(Keys.ENTER)

    def mega_menu_products_click(self):
        MEGA_MENU_PRODUCTS = self.driver.find_element(By.CSS_SELECTOR,'body > nav > div > ul.c-mm-condensed__top-items.u-mt-sm-5 > li:nth-child(2) > a')
        MEGA_MENU_PRODUCTS.click()

    def left_menu_mortgage_check(self):
        LEFT_MENU_MORTGAGES = self.driver.find_element(By.CSS_SELECTOR,'li.has-children:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').text
        return LEFT_MENU_MORTGAGES

    def mega_menu_services_click(self):
        MEGA_MENU_SERVICES = self.driver.find_element(By.CSS_SELECTOR,'body > nav > div > ul.c-mm-condensed__top-items.u-mt-sm-5 > li:nth-child(3) > a')
        MEGA_MENU_SERVICES.click()

    def current_account_services_check(self):
        CURRENT_ACCOUNT_SERVICES = self.driver.find_element(By.CSS_SELECTOR,'body > nav > div > ul.c-mm-condensed__top-items.u-mt-sm-5 > li.has-children.is-active > div > div.medium-8.c-mm-condensed__col > h4.u-font-size-1-5rem.u-font-size-1-25rem-sm.u-font-light.u-mt-0.u-mb-3').text
        return CURRENT_ACCOUNT_SERVICES

