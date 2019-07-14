from pages.base_page import BasePage
from behave import *
from selenium.webdriver.common.by import By


@step('I navigate to the Bank Homepage')
def step_impl(context):
    page = BasePage()
    page.navigate("https://www.bankofireland.com/")
    #assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")
