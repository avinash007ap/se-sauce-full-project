from selenium.webdriver.common.by import By
from base import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.CART_ITEMS_CLASS = (By.CLASS_NAME, "cart_item")
        self.CART_QUANTITIES_CLASS = (By.CLASS_NAME, "cart_quantity")
        self.CHECKOUT_BUTTON_ID = (By.ID, "checkout")
        self.CONTINUE_SHOPPING_ID = (By.ID, "continue-shopping")
        self.REMOVE_BUTTONS_XPATH = (By.XPATH, "//button[contains(@class='cart_button')]")

    def get_cart_items(self):
        return self.driver.find_elements(self.CART_ITEMS_CLASS)
    
    def get_cart_quantity(self):
        return self.driver.find_elements(self.CART_QUANTITIES_CLASS)
    
    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON_ID)
        return self
    
    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_ID)
        return self
    
    def remove_all_items(self):
        remove_buttons = self.driver.find_elements(self.REMOVE_BUTTONS_XPATH)
        for button in remove_buttons:
            button.click()
        return self
    

    
