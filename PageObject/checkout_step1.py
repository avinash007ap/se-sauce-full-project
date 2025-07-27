from selenium.webdriver.common.by import By
from base import BasePage

class CheckoutPage(BasePage):
    def _init__(self, driver):
        self.driver = driver
        self.CHECKOUT_BUTTON_NAME = (By.NAME, "checkout")
        self.CHECKOUT_INFO_CLASS = (By.CLASS_NAME, "checkout_info")
        self.FIRSTNAME_NAME = (By.NAME, "firstName")
        self.LASTNAME_NAME = (By.NAME, "lastName")
        self.POSTALCODE_NAME = (By.NAME, "postalCode")
        self.CHECKOUT_SUBMIT_XPATH = (By.XPATH, "//input[@type='submit']")
        self.CHECKOUT_FINISH_XPATH = (By.XPATH, "//button[@id='finish']")
        self.ORDER_CONFIRM_HEADER_NAME = (By.XPATH, "//h2[@class='complete-header']")
    
    def navigate_to_checkout(self):
        self.find_element(self.CHECKOUT_BUTTON_NAME).click()
        self.find_element()
        self.find_element(self.CHECKOUT_INFO_CLASS)
        return self
    
    def checkout_fill_details(self, first_name="John", last_name="Doe", postal_code="973865"):
        self.find_element(self.FIRSTNAME_NAME).send_keys(first_name)
        self.find_element(self.LASTNAME_NAME).send_keys(last_name)
        self.find_element(self.POSTALCODE_NAME).send_keys(postal_code)
        self.find_element(self.CHECKOUT_SUBMIT_XPATH).click()

    def confirm_order(self):
        self.find_element(self.CHECKOUT_FINISH_XPATH).click()
        order_confirm = driver.find_element(self.ORDER_CONFIRM_HEADER_NAME).text
        return order_confirm
        #assert order_confirm == "Thank you for your order!", "Order not placed due to technical issues"

        
    