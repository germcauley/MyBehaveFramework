from behave import *
import time
from hamcrest import *
'''

@Given('I open BOI homepage')
def step_impl(context):
    context.home_page.navigate('https://www.bankofireland.com/')

@When('I click the cookie accept button')
def step_impl(context):
    context.home_page.click_cookie

@When('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)
    
'''

@Given('I navigate to BOI homepage')
def step_impl(context):
    context.home_page.navigate('https://www.bankofireland.com/')

@When('I click the Cookie accept button')
def step_impl(context):
    context.home_page.click_cookie()
    time.sleep(5)


@When('I click products in the mega menu')
def step_impl(context):
    context.home_page.mega_menu_products_click()


@Then('Mortgages tab appears')
def step_impl(context):
    assert_that(context.home_page.left_menu_mortgage_check(),equal_to_ignoring_case('mortgages'))

@When('I click "Services" in mega menu')
def step_impl(context):
    context.home_page.mega_menu_services_click()

# @Then('"Current account services" is visible')
# def step_impl(context):
#     assert_that(context.home_page.current_account_services_check()
