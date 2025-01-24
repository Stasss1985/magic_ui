from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage


class CustomerLogin(BasePage):
    page_url = '/customer/account/login'

    def fill_login_form(self, login, password):
        email_fild = self.driver.find_element(By.ID, 'email')
        password_fild = self.driver.find_element(By.ID, 'pass')
        button = self.driver.find_element(By.ID, 'send2')
        email_fild.send_keys(login)
        password_fild.send_keys(password)
        button.click()

    def check_error_alert_is(self, text):
        error_alert = self.driver.find_element(
            By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'
        )
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(error_alert))
        assert error_alert.text == text
