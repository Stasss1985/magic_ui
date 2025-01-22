import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from time import sleep

@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    return chrome_driver

