from selenium import webdriver
from selenium.webdriver.common.by import By

class InventoryPage:
    """
    Clase que contiene los elementos de la página de Inventory
    """
    def __init__(self, driver: webdriver.Remote):
        self.driver = driver
    
    @property
    def __span_title(self):
        return self.driver.find_element(By.CLASS_NAME, "title")
    
    @property
    def __button_add_to_cart(self):
        return self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    
    @property
    def __a_shopping_cart(self):
        return self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    
# Funciones que se encargan de interactuar con los elementos de la página

    def obtener_titulo(self):
        """
        Método que se encarga de obtener el título de la página
        Return: título de la página
        """
        return self.__span_title.text
    
    def agregar_producto(self):
        """
        Método que se encarga de agregar un producto al carrito
        """
        self.__button_add_to_cart.click()
    
    def ir_al_carrito(self):
        """
        Método que se encarga de ir al carrito
        """
        self.__a_shopping_cart.click()