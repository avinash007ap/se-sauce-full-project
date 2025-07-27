import pytest
from selenium import webdriver

from PageObject.login import LoginPage
from PageObject.shop import ShopPage
from config import Config

class TestShop():       
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.open(Config.BASE_URL)
        self.shop_page = ShopPage(self.driver)
    
    def teardown(self):
        self.driver.quit()

    @pytest.fixture
    def get_elements(self):
        elements = self.shop_page.check_products_exist_css()
        return elements
    
    def test_elements_exist(self,get_elements):
        assert get_elements != 0, "No elements found"

    def test_elements_text(self, get_elements):
        text = self.shop_page.fetch_text_of_products(get_elements)
        assert text != [], "Elements text value is not returned properly"

    def test_elements_count(self, get_elements):
        count = self.shop_page.fetch_len_of_products(get_elements)
        assert count > 0, "Elemnets count must be greater than zero"

    def test_products_added(self, count):
        added_count = self.shop_page.add_products_to_cart(count)
        cart_count = self.shop_page.validate_products_added()
        assert added_count == cart_count, "Products are not added correctly"

    #@pytest.mark.parametrize(product_name=['', ''])
    def test_added_product_name(self, product_name):
        pass

    def test_sort_product_low_to_high(self):
        option_selected = self.shop_page.sort_products_low_to_high()
        assert option_selected == "Price (low to high)", "Option is not selected correctly"

    def test_cart_items_null_after_reset(self):
        cart_count = self.shop_page.validate_products_added()
        assert cart_count != 0, "No items added in cart,nothing to reset"
        self.shop_page.reset_cart()
        cart_count_after_reset = self.shop_page.validate_products_added()
        assert cart_count_after_reset == 0, "Cart items still exist, reset button not working"
        