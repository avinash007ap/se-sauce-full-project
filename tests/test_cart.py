import pytest
from selenium import webdriver

from PageObject.login import LoginPage
from PageObject.shop import ShopPage
from PageObject.cart import CartPage
from config import Config

class TestCart():       
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.open(Config.BASE_URL)
        self.shop_page = ShopPage(self.driver)
        self.cart_page = CartPage(self.driver)
    
    def teardown(self):
        self.driver.quit()

    def test_cart_added_count(self):
        cart_items = self.cart_page.get_cart_items()
        cart_quantity = self.cart_page.get_cart_quantity()
        if cart_items != None:
            assert len(cart_items) == cart_quantity, "Cart items and quantity are not matching"
        else:
            raise Exception("Cart items are not returned")
           
    def test_cart_removed_successfully(self):
        cart_quantity = self.cart_page.get_cart_quantity()
        assert cart_quantity != 0, "Nothing to remove in cart"
        self.remove_all_items()
        cart_quantity_after = self.cart_page.get_cart_quantity()
        assert cart_quantity_after == 0, "Cart items not removed properly"





    