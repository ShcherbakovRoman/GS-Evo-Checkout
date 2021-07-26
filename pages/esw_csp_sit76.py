from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.evo_checkout import Evo_Checkout


class CSP_sit76(Page):
    LOGIN_BTN = (By.ID, 'loginLink')
    USER_NAME = (By.ID, 'txtUserName')
    PW = (By.ID, 'Password')
    SUBMIT_LOGIN = (By.ID, 'btnLogin')
    CS_DROPDOWN = (By.ID, 'lnkCustomerService')
    ORDER_SEARCH = (By.XPATH, '//a[text()="Search for Order"]')
    ORDER_NUMBER_FIELD = (By.ID, 'txtCustomerRefs')
    SUBMIT_SEARCH = (By.ID, 'btnSearchSubmit')
    ORDER_NUMBER_DISPLAY = (By.XPATH, '//td[contains(text(),"ESW")]')

    def enter_csp(self, end_point):
        if end_point == "SIT76":
            self.open_page('https://sit76-csp.nike.eshopworld.net/')
            self.click(*self.LOGIN_BTN)
            self.input_text('roman.shcherbakov@nike.com', *self.USER_NAME)
            self.input_text('Shch-r0man', *self.PW)
            self.click(*self.SUBMIT_LOGIN)
        else:
            self.open_page('https://preprod-csp.nike.eshopworld.net/')
            self.click(*self.LOGIN_BTN)
            self.input_text('roman.shcherbakov@nike.com', *self.USER_NAME)
            self.input_text('R0man-shch', *self.PW)
            self.click(*self.SUBMIT_LOGIN)

    def open_customer_service(self):
        self.click(*self.CS_DROPDOWN)
        self.click(*self.ORDER_SEARCH)

    def order_search_and_confirm(self):
        for order_number in Evo_Checkout.confirmation_numbers:
            self.input_text(order_number, *self.ORDER_NUMBER_FIELD)
            self.click(*self.SUBMIT_SEARCH)
            self.wait_for_element_appear(*self.ORDER_NUMBER_DISPLAY)
            self.verify_text(order_number, *self.ORDER_NUMBER_DISPLAY)
            self.refresh_page()
        print(Evo_Checkout.confirmation_numbers)






