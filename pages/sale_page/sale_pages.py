from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.sale_page import sale_locators as loc

class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        assert header_title.text == text
