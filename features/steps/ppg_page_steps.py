from behave import *
from pages.ppg_page import PPGPage
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


@step('I navigate to PPG')
def step_impl(context):
    page = PPGPage(context)
    page.navigate("https://personalbanking.bankofireland.com/borrow/mortgages/")