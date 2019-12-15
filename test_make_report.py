import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from time import time


def test_register_new_user(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.register_new_user(str(time()) + '@testmail.org', 'truepassw')
    login_page.should_be_login_icon()
    login_page.should_be_success_register_message()
