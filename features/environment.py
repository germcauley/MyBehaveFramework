
from selenium import webdriver
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.ppg_page import PPGPage
# from pages.search_results_page import SearchResultsPage

def before_all(context):
    context.base_page = BasePage
    context.home_page = HomePage
    context.ppg_page = PPGPage
    # context.search_results_page = SearchResultsPage()


# def after_all(context):
#     BasePage.close()



