from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from base import BasePage
from PageObject.login import LoginPage
from config import Config

@given("user is on login page")
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open(Config.BASE_URL)

@when("user enters valid credentials")
def step_impl(context):
    context.login_page.login(Config.STANDARD_USER, Config.PASSWORD)

@then("user should land on dashboard")
def step_impl(context):
    assert Config.LOGIN_SUCCESS_URL in context.driver.current_url
