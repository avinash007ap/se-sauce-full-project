from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import Config


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, Config.EXPLICIT_WAIT)
        self.allowed_headers = ["h" + str(i) for i in range(1, 7)]
        self.header_xpath = (By.XPATH, "tag")

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator):
        element = self.find_element(locator)
        element.clear()
        element.send_keys()

    def is_element_present(self, locator):
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False
        
    def get_title(self):
        return self.driver.title
    
    def get_header(self, header_type):
        if header_type in self.allowed_headers:
            self.header_xpath[1].replace("tag", header_type)
            return self.find_element(self.header_xpath)
