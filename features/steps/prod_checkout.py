from behave import given, when, then
from time import sleep



@given('Open Nike.com for {country}')
def open_home_page(context, country):
    context.app.home_page.open_home_page(country)
    context.app.home_page.confirm_location()


@when('Open any category')
def open_product_category(context):
    context.app.home_page.hover_over_menu()
    context.app.home_page.select_from_menu()


@when('Select any Product')
def select_product(context):
    context.app.pw.select_product()

@when('Select Size and add to Cart')
def select_size_and_add_to_cart(context):
    context.app.pdp.select_size()
    context.app.pdp.add_to_bag()

@when('Go to Cart')
def go_to_cart(context):
    context.app.pdp.go_to_cart()

@when('Proceed to Checkout as {user}')
def enter_checkout(context, user):
    user = user.lower()
    if user == 'guest':
        context.app.cart.guest_checkout()
    else:
        context.app.cart.member_checkout()


