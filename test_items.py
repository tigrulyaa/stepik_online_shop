from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_can_add_to_cart(browser):
    try:
        browser.get(link)
        assert browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form > button")
    finally:
        print('end')
