import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class SampleTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Firefox()


    def pypi_test(self):

        driver = webdriver.Firefox()
        driver.get("https://pypi.python.org/pypi")
        driver.find_element(By.ID, "search").send_keys("Selenium")
        driver.find_element(By.CLASS_NAME, "search-form__button").click()
        driver.quit()

    def tearDown(self):
        self.driver.quit()

