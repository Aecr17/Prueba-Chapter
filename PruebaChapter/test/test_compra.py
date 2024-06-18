import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium import webdriver

class TestCompra:
    def test_compra(self, driver:webdriver.Remote):
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        driver.get("https://www.saucedemo.com/")
        login_page.login_completo("standard_user", "secret_sauce")
        inventory_page.agregar_producto()
        inventory_page.ir_al_carrito()
        