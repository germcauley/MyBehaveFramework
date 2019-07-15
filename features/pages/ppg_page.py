from pages.base_page import BasePage


class PPGPage(BasePage):

    def ppgrefresh(context):
        context.driver.refresh()