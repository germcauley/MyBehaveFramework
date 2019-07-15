from behave import *
from selenium.webdriver.common.by import By


@step('I navigate to the Google')
def step_impl(context):
    context.base_page.navigate("https://www.google.ie")
    #assert_equal(context.home_page.get_page_title(), "PyPI - the Python Package Index : Python Package Index")