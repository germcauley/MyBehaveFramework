from pages.base_page import BasePage


class HomePage(BasePage):

    def refresh(context):
        context.driver.refresh()

