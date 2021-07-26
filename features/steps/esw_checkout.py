from behave import given, when, then
from time import sleep


user = 'nike-qa-iis'
pw = 'FSCEo7qHi1w'


@given('Enter eSW test harness')
def enter_eswharness(context):
    context.app.esw_harness.enter_harness(user, pw)

@when('Select end-point - {endpoint}')
def select_endpoint(context, endpoint):
    context.app.esw_harness.select_endpoint(endpoint)

@when('Select JSON: Number of lines - {line_qty}; XA/XP - {merch_group}')
def select_json(context, line_qty, merch_group):
    context.line_qty = line_qty
    context.app.esw_harness.select_json(line_qty, merch_group)

@when('Select country - {country}')
def select_country(context, country):
    context.country = country
    context.app.esw_harness.select_country(country)

@when('Select language - English')
def select_lang(context):
    context.app.esw_harness.select_language()

@when('Select QTY - {product_qty}')
def select_product_qty(context, product_qty):
    context.product_qty = product_qty
    context.app.esw_harness.select_product_qty(product_qty)

@when('Change price to 50')
def change_price(context):
    context.app.esw_harness.change_price()

@when('Enter Checkout')
def enter_checkout(context):
    context.app.esw_harness.submit_payload()

@then('Verify quantity in Checkout is correct')
def verify_qty(context):
    context.app.evo_checkout.verify_qty_in_checkout(context.product_qty)

@then('Verify if EVO Checkout is invoked')
def verify_evo(context):
    context.app.evo_checkout.verify_evo_checkout()

@when('Enter all shipping info')
def enter_ship_details(context):
    context.app.evo_checkout.enter_ship_details()

@when('Enter all shipping info for AU')
def enter_ship_details_au(context):
    context.app.evo_checkout.enter_ship_details_au()

@when('Enter all shipping info for NO')
def enter_ship_details_no(context):
    context.app.evo_checkout.enter_ship_details_no()

@when('Enter all shipping info for SG')
def enter_ship_details_sg(context):
    context.app.evo_checkout.enter_ship_details_sg()

@when('Enter all shipping info for MX')
def enter_ship_details_mx(context):
    context.app.evo_checkout.enter_ship_details_mx()

@when('Enter all shipping info for TR')
def enter_ship_details_tr(context):
    context.app.evo_checkout.enter_ship_details_tr()

@when('Enter all shipping info for RU')
def enter_ship_details_ru(context):
    context.app.evo_checkout.enter_ship_details_ru()

@when('Enter all shipping info for CH')
def enter_ship_details_ch(context):
    context.app.evo_checkout.enter_ship_details_ch()

@when('Enter all shipping info for NZ')
def enter_ship_details_nz(context):
    context.app.evo_checkout.enter_ship_details_nz()

@when('Enter all shipping info for ZA')
def enter_ship_details_za(context):
    context.app.evo_checkout.enter_ship_details_za()

@when('Enter all shipping info for IL')
def enter_ship_details_il(context):
    context.app.evo_checkout.enter_ship_details_il()

@when('Enter all shipping info for RO')
def enter_ship_details_ro(context):
    context.app.evo_checkout.enter_ship_details_ro()

@when('Enter all shipping info for UAE')
def enter_ship_details_uae(context):
    context.app.evo_checkout.enter_ship_details_uae()

@when('Enter all shipping info for SA')
def enter_ship_details_sa(context):
    context.app.evo_checkout.enter_ship_details_sa()

@when('Enter all shipping info for BG')
def enter_ship_details_bg(context):
    context.app.evo_checkout.enter_ship_details_bg()

@when('Enter all shipping info for SK')
def enter_ship_details_sk(context):
    context.app.evo_checkout.enter_ship_details_sk()

@when('Enter all shipping info for HR')
def enter_ship_details_hr(context):
    context.app.evo_checkout.enter_ship_details_hr()

@when('Enter all shipping info for VN')
def enter_ship_details_vn(context):
    context.app.evo_checkout.enter_ship_details_vn()

@when('Enter all shipping info for IN')
def enter_ship_details_in(context):
    context.app.evo_checkout.enter_ship_details_in()

@when('Enter all shipping info for MA')
def enter_ship_details_ma(context):
    context.app.evo_checkout.enter_ship_details_ma()

@when('Enter all shipping info for PH')
def enter_ship_details_ph(context):
    context.app.evo_checkout.enter_ship_details_ph()

@when('Enter all shipping info for ID')
def enter_ship_details_id(context):
    context.app.evo_checkout.enter_ship_details_id()

@when('Enter all shipping info for TW')
def enter_ship_details_tw(context):
    context.app.evo_checkout.enter_ship_details_tw()

@when('Enter all shipping info for TH')
def enter_ship_details_th(context):
    context.app.evo_checkout.enter_ship_details_th()

@when('Select delivery method - {ship_method}')
def select_shipping(context, ship_method):
    context.app.evo_checkout.select_shipping_method(ship_method)

@when('Confirm billing info')
def confrim_billing(context):
    context.app.evo_checkout.confirm_billing()

@when('Enter payment details')
def enter_payment_details(context):
    context.app.evo_checkout.enter_payment()

@when('Enter payment details for TR')
def enter_tr_payment_details(context):
    context.app.evo_checkout.enter_tr_payment()

@when('Give consent')
def give_consent(context):
    context.app.evo_checkout.check_pay_consent()

@when('Submit an order')
def submit_order(context):
    context.app.evo_checkout.submit_order()

@when('Confirm successful payment')
def confirm_success_pmnt(context):
    context.app.evo_checkout.confirm_success_pmnt()

@when('Submit SMS code')
def submit_sms_code(context):
    context.app.evo_checkout.submit_sms_code()

@then('Verify if "Place Order" button is enabled')
def verify_submit_button(context):
    context.app.evo_checkout.verify_submit_button()

@then('Verify if Order Confirmation page is displayed')
def order_confirmation_page(context):
    context.app.evo_checkout.order_confirmation_page()

@then('Verify quantity is correct on confirmation page')
def verify_qty_in_confirmation(context):
    context.app.evo_checkout.verify_qty_in_confirmation(context.product_qty)

@then('Verify if correct number of products is displayed')
def verify_number_of_product_lines(context):
    context.app.evo_checkout.verify_number_of_product_lines(context.line_qty)

@when('Click "Become Member" CTA')
def click_become_member(context):
    context.app.evo_checkout.become_member_cta()

@when('Enter new member details and submit')
def enter_new_member_details(context):
    context.app.evo_checkout.new_member_details()

@when('Click "Login" CTA')
def click_login(context):
    context.app.evo_checkout.click_login()

@when('Enter Member details and submit')
def enter_login_info(context):
    context.app.evo_checkout.enter_login_info()

@then('Verify if consumer is in logged-in state')
def verify_user_loggedin(context):
    context.app.evo_checkout.verify_loggedin_state()

@then('Verify if consumer is in logged-in state for TR')
def verify_user_loggedin(context):
    context.app.evo_checkout.verify_loggedin_state_tr()

@when('Enter old Member details and submit')
def enter_login_info(context):
    context.app.evo_checkout.enter_member_w_address_info()

@then('Verify saved address is invoked')
def verify_saved_address_present(context):
    context.app.evo_checkout.verify_saved_address_present()

@when('Click Continue')
def click_continue(context):
    context.app.evo_checkout.click_continue()

@then('Verify Member card presence')
def verify_saved_cc_present(context):
    context.app.evo_checkout.verify_saved_cc_present()

@then('Verify EDDs are matching')
def compare_edds(context):
    context.app.evo_checkout.compare_edds()

@when('Enter NOT all shipping info')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details()

@when('Enter NOT all shipping info for AU')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_au()

@when('Enter NOT all shipping info for SG')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_sg()

@when('Enter NOT all shipping info for MX')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_mx()

@when('Enter NOT all shipping info for TR')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_tr()

@when('Enter NOT all shipping info for RU')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_ru()

@when('Enter NOT all shipping info for CH')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_ch()

@when('Enter NOT all shipping info for NO')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_no()

@when('Enter NOT all shipping info for NZ')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_nz()

@when('Enter NOT all shipping info for ZA')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_za()

@when('Enter NOT all shipping info for IL')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_il()

@when('Enter NOT all shipping info for RO')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_ro()

@when('Enter NOT all shipping info for UAE')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_uae()

@when('Enter NOT all shipping info for SA')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_sa()

@when('Enter NOT all shipping info for BG')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_bg()

@when('Enter NOT all shipping info for SK')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_sk()

@when('Enter NOT all shipping info for HR')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_hr()

@when('Enter NOT all shipping info for VN')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_vn()

@when('Enter NOT all shipping info for IN')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_in()

@when('Enter NOT all shipping info for MA')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_ma()

@when('Enter NOT all shipping info for PH')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_ph()

@when('Enter NOT all shipping info for ID')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_id()

@when('Enter NOT all shipping info for TW')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_tw()

@when('Enter NOT all shipping info for TH')
def enter_invalid_ship_info(context):
    context.app.evo_checkout.enter_invalid_ship_details_th()

@then('Verify if Continue button is inactive')
def verify_inactive_continue_btn(context):
    context.app.evo_checkout.verify_continue_btn_inactive()

@when('Enter missing shipping info')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info()

@when('Enter missing shipping info for AU')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_au()

@when('Enter missing shipping info for SG')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_sg()

@when('Enter missing shipping info for MX')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_mx()

@when('Enter missing shipping info for TR')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_tr()

@when('Enter missing shipping info for RU')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_ru()

@when('Enter missing shipping info for CH')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_ch()

@when('Enter missing shipping info for NO')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_no()

@when('Enter missing shipping info for ZA')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_za()

@when('Enter missing shipping info for IL')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_il()

@when('Enter missing shipping info for RO')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_ro()

@when('Enter missing shipping info for UAE')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_uae()

@when('Enter missing shipping info for SA')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_sa()

@when('Enter missing shipping info for BG')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_bg()

@when('Enter missing shipping info for SK')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_sk()

@when('Enter missing shipping info for HR')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_hr()

@when('Enter missing shipping info for VN')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_vn()

@when('Enter missing shipping info for IN')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_in()

@when('Enter missing shipping info for MA')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_ma()

@when('Enter missing shipping info for PH')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_ph()

@when('Enter missing shipping info for ID')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_id()

@when('Enter missing shipping info for TW')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_tw()

@when('Enter missing shipping info for TH')
def enter_phone_number(context):
    context.app.evo_checkout.add_missing_ship_info_th()

@then('Verify if next page is displayed')
def verify_ship_speed_page(context):
    context.app.evo_checkout.verify_shipping_speed_page()

@then('Verify if Continue button is clickable')
def verify_continue_btn_clickable(context):
    context.app.evo_checkout.verify_continue_btn_clickable()

@when('Uncheck the Billing info box')
def uncheck_billing_box(context):
    context.app.evo_checkout.click_billing_checkbox()

@then('Verify the Billing address is empty')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty()

@then('Verify the Billing address is empty for MX')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty_mx()

@then('Verify the Billing address is empty for TR')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty_tr()

@then('Verify the Billing address is empty for RU')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty_ru()

@then('Verify the Billing address is empty for UAE')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty_uae()

@then('Verify the Billing address is empty for TH')
def verify_billing_matches_shipping(context):
    context.app.evo_checkout.verify_billing_empty_th()

@then('Verify if calculations in Subtotal are correct')
def verify_subtotal_calculations(context):
    context.app.evo_checkout.verify_calculations()

@then('Verify if calculations in Subtotal are correct - big numbers')
def verify_subtotal_calculations(context):
    context.app.evo_checkout.verify_calculations_bn()

@given('Enter eSW CSP tool on {end_point}')
def enter_csp_tool_sit76(context, end_point):
    context.app.esw_csp_sit76.enter_csp(end_point)

@when('Open Customer Service page')
def open_cs_page(context):
    context.app.esw_csp_sit76.open_customer_service()

@then('Search for order and verify it is in CSP')
def search_order(context):
    context.app.esw_csp_sit76.order_search_and_confirm()

