from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage
from pages.login_pages import login_locators as loc


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_fild = self.find(loc.email_fild_loc)
        password_fild = self.find(loc.password_fild_loc)
        button = self.find(loc.button_loc)
        email_fild.send_keys(login)
        password_fild.send_keys(password)
        button.click()

    def check_error_alert_is(self, text):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(loc.error_alert_loc))
        error_alert = self.find(loc.error_alert_loc)
        assert error_alert.text == text
