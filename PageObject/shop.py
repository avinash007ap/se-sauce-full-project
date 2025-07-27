from selenium import webdriver
from selenium.webdriver.common.by import By
from base import BasePage

class ShopPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.PRODUCT_NAMES_CSS = (By.CSS_SELECTOR, "a[id='^item_'] div[class='inventory_item_name ']")
        self.PRODUCT_LINK_CSS = (By.CSS_SELECTOR, "a[id^='item_']")
        self.PRODUCT_DIVS_CSS = (By.CSS_SELECTOR, "div.inventory_item_name")
        self.PRODUCT_DIVS_XPATH = (By.XPATH, "//div[@id='inventory_container']")
        self.ADD_TO_CART_CSS = (By.CSS_SELECTOR, ".btn")
        self.SORT_PRODUCT_CLASS = (By.CLASS_NAME, "product_sort_container")
        self.SORT_OPTION_LOHI_XPATH = (By.XPATH, "//option[@value='lohi']")
        self.SHOPPING_CART_BUTTON_XPATH = (By.XPATH, "//a[@class='shopping_cart_link']")
        self.CART_QUANTITY_CLASS = (By.XPATH, "//div[@class='cart_quantity']")
        self.BURGER_MENU_BUTTON_XPATH = (By.XPATH, "//button[@id='react-burger-menu-btn']")
        self.RESET_BUTTON_XPATH = (By.XPATH, "//a[@id='reset_sidebar_link']")

    def check_products_exist_css(self):
        # self.find_element(self.PRODUCT_NAMES_CSS)    
        elements = self.driver.find_elements(self.PRODUCT_NAMES_CSS)
        return elements
    
    def fetch_text_of_products(self, web_elements):
        text_list = []
        if web_elements != None:
            for element in web_elements:
                text_list.append(element.text)
        return text_list

    
    def fetch_len_of_products(self, web_elements):
        element_count = 0
        if web_elements != None:
            element_count = len(web_elements)
        return element_count

    def add_products_to_cart(self, product_count):
        added_count = 0
        add_to_cart_btn = self.driver.find_elements(self.ADD_TO_CART_CSS)
        for i in range(product_count):
            add_to_cart_btn[i].click()
            print(f"Added product - {i} to cart")
            added_count += 1
        return added_count
    
    def validate_products_added(self):     
        self.find_element(self.SHOPPING_CART_BUTTON_XPATH).click()
        cart_items = self.driver.find_elements(self.CART_QUANTITY_CLASS)
        cart_count = len(cart_items)
        return cart_count
    
    def sort_products_low_to_high(self):
        self.driver.click(self.SORT_PRODUCT_CLASS)
        option = self.driver.click(self.SORT_OPTION_LOHI_XPATH)
        print(f"Option value = {option.text}")
        return option.text

    def sort_products_based_on_option(self, option_code):
        pass

    def reset_cart(self):
        self.find_element(self.BURGER_MENU_BUTTON_XPATH).click()
        self.find_element(self.RESET_BUTTON_XPATH).click()
        return self



        

