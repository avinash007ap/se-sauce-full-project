import pytest
from selenium import webdriver
#from selenium.webdriver.common import By
from PageObject.login import LoginPage
from config import Config

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.open(Config.BASE_URL)

    def teardown(self):
        self.driver.quit()

    def test_successful_login(self):
        #self.login_page.open(Config.BASE_URL)
        #self.login_page.login()
        self.login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        assert Config.LOGIN_SUCCESS_URL in self.driver.current_url

    def test_unsuccessful_login(self):
        #self.login_page.open(Config.BASE_URL)
        self.login_page.login(Config.STANDARD_USER, Config.PASSWORD)
        

