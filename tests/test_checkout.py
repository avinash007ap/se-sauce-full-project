import pytest
from selenium import webdriver

from PageObject.login import LoginPage
from PageObject.checkout_step1 import CheckoutPage
from config import Config

class TestShop():       
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.open(Config.BASE_URL)
        self.checkout_page = CheckoutPage(self.driver)
    
    def teardown(self):
        self.driver.quit()

    def checkout_details(self, ):
        navigate_to_checkout()
        
    def test_order_confirmed(self):
        order_confirm = self.checkout_page.confirm_order()
        assert order_confirm == "Thank you for your order!", "Order not placed due to technical issues"

    