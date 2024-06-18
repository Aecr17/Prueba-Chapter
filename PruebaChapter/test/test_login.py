import pytest
from pages.login_page import LoginPage
from selenium import webdriver

class TestLogin:
    def test_login(self, driver:webdriver.Remote):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login_completo("standard_user", "secret_sauce")
        login_page.test_get_title()
        
    def test_locked_user(self, driver:webdriver.Remote):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login_completo("locked_out_user,", "secret_sauce")

    def test_problem_user(self, driver:webdriver.Remote):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login_completo("problem_user", "secret_sauce")