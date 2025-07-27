from behave import given, when, then
from PageObject.cart import CartPage

@given("User is on cart page with non empty items")
def step_imp(context):
    context.cart_page = CartPage(context.driver)
    context.cart_quantity = context.cart_page.get_cart_quantity()
    assert context.cart_quantity != 0, "Nothing to remove in cart"

@when("User removes all items from cart")
def step_impl(context):
    context.cart_page.remove_all_items()

@then("Cart quantity should be empty")
def step_impl(context):
    context.cart_quantity_after = context.cart_page.get_cart_quantity()
    assert context.cart_quantity_after == 0, "Cart items not removed properly"
