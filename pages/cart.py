from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Cart(Page):
    GUEST_CHECKOUT = (By.CSS_SELECTOR, '[data-automation=guest-checkout-button]')
    MEMBER_CHECKOUT = (By.CSS_SELECTOR, '[data-automation=member-checkout-button]')
    SUBTOTAL = (By.CSS_SELECTOR, '[data-automation=summary-subtotal] .price')

    def guest_checkout(self):
        self.wait_for_clickable_element(*self.GUEST_CHECKOUT)
        self.click(*self.GUEST_CHECKOUT)
        sleep(2)

    def member_checkout(self):
        self.wait_for_clickable_element(*self.MEMBER_CHECKOUT)
        self.click(*self.MEMBER_CHECKOUT)