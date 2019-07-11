from behave import *
import time
from hamcrest import *


@step('I navigate to BB homepage')
def step_impl(context):
     context.business_banking_page.navigate('https://businessbanking.bankofireland.com/')


@When('I click the accept cookie button')
def step_impl(context):
    context.business_banking_page.cookie_click()

@When('I search for "{search_term}"')
def step_impl(context, search_term):
    context.business_banking_page.search_bca(search_term)

# @Then('I check the BCA Features url is in the results')
# def step_impl(context):
#     assert_that(context.business_banking_page.search_bca(search_term),equal_to_ignoring_case('Business Current Account - Business Accounts | Bank of Ireland'))
