import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SampleTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/darren/PycharmProjects/new-framework/chromedriver')

    def tearDown(self):
        self.driver.quit()