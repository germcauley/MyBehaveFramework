from selenium import webdriver

class Browser(object):

    def __init__(self, context):
        # context.driver = webdriver.Chrome('/Users/darren/PycharmProjects/new-framework/chromedriver')
        self.context = context
        self.context.driver = webdriver.Chrome()
        self.timeout = 30

    def close(context):
        context.driver.close()