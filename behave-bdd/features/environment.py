from selenium import webdriver
from PageObject.login import LoginPage
from config import Config


def before_all(context):
    print("Test session starts")
    context.driver = webdriver.Chrome()
    context.login_page = LoginPage(context.driver)
    context.login_page.open(Config.BASE_URL)
    context.login_page.login(Config.STANDARD_USER, Config.PASSWORD)

def after_all(context):
    print("Test session ends")
    context.driver.quit()