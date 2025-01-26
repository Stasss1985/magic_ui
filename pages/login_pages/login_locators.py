from selenium.webdriver.common.by import By

email_fild_loc = (By.ID, 'email')
password_fild_loc = (By.ID, 'pass')
button_loc = (By.ID, 'send2')
error_alert_loc = (By.CSS_SELECTOR, '[data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
