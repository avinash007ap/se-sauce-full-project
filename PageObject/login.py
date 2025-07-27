from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.username_inp = (By.ID, "user-name")
        self.password_inp = (By.ID, "password")
        self.login_button = (By.ID, "login-button")        

    def login(self, username=None, password=None):
        self.driver.find_element(self.username_inp).send_keys(username)
        self.driver.find_element(self.password_inp).send_keys(password)
        self.driver.find_element(self.login_button).click()
        return self
    
    def open(self, url):
        self.driver.get(url)
        return self
        