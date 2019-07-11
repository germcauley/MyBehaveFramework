from selenium import webdriver

class Browser(object):

    def __init__(context):
        context.driver = webdriver.Chrome()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(30)
        context.driver.maximize_window()

    def close(context):
        context.driver.close()