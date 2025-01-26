import pytest
from selenium import webdriver
from time import sleep
from pages.sale_page.sale_pages import SalePage
from pages.login_pages.customer_login import CustomerLogin

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    return chrome_driver

@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)

@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)

