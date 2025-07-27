from behave import given, when, then
from PageObject.login import LoginPage
from PageObject.shop import ShopPage
from config import Config


@given("user is on product page")
def step_impl(context):
    context.shop_page = ShopPage(context.driver)
    context.shop_page.check_products_exist_css()

@when("they click 'Add to cart'")
def step_impl(context):
    context.added_count = context.shop_page.add_products_to_cart(Config.PRODUCT_COUNT)

@then("item should appear in cart ")
def step_impl(context):
    context.cart_count = context.shop_page.validate_products_added()
    assert context.added_count == context.cart_count, "There is mismatch in added & cart items"
