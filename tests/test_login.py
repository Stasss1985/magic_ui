
def test_incorrect_login(login_page):
    login_page.open_page()
    login_page.fill_login_form('dfjasldk@mail.ru', '56224f')
    login_page.check_error_alert_is(
        'The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.')


def test_correct_email_with_incorrect_password(login_page):
    login_page.open_page()
    login_page.fill_login_form('dfjasldk@mail.ru', '56224f')
    login_page.check_error_alert_is('Здесь другая ошибка и текст.')
