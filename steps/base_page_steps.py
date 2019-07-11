from hamcrest import *
import time
from behave import *


@step('I refresh the page')
def step_impl(context):
    context.basepage.refresh()
    time.sleep(3)

# @step('I click the accept cookie button')
# def step_impl(context):
#     context.basepage.cookie_click()