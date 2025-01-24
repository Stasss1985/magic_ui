from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.driver.find_element(By.TAG_NAME, 'h1')
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(header_title))
        assert header_title.text == text
