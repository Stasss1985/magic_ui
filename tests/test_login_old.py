import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils import project_ec


#def test_incorrect_login(driver):
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    email_fild = driver.find_element(By.ID, 'email')
    password_fild = driver.find_element(By.ID, 'pass')
    button = driver.find_element(By.ID, 'send2')
    email_fild.send_keys('dfjasldk@mail.ru')
    password_fild.send_keys('56224f')
    button.click()
    error_alert = driver.find_element(
        By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]'
    )
    WebDriverWait(driver, 5).until(project_ec.text_is_not_empty_in_element(error_alert))
    assert error_alert.text == (
        "The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later."
    )
