from pages.base_page import BasePage


class HomePage(BasePage):

    def wwwrefresh(context):
        context.driver.refresh()

