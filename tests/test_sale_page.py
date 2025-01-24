from pages.sale_pages import SalePage

def test_header_title(driver):
    sale_page = SalePage(driver)
    sale_page.open_page()
    sale_page.check_page_header_title_is('Sale')
