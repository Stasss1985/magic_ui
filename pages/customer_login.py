
class CustomerLogin:

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get('https://magento.softwaretestingboard.com/customer/account/login')