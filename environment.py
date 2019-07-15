# Setting up the test environment to run the tests (what browsers, pages used)

from browser import Browser
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.business_banking_page import BBPAGE

def before_all(context):
    context.browser = Browser
    context.basepage = BasePage
    context.home_page = HomePage
    context.business_banking_page = BBPAGE
    # context.search_results_page = SearchResultsPage()

def after_all(context):
    context.browser.close()