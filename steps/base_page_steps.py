from hamcrest import *

from behave import *

@step('I refresh the page')
def step_impl(context):
    context.basepage.refresh()

# @step('I click the accept cookie button')
# def step_impl(context):
#     context.basepage.cookie_click()