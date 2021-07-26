from selenium.webdriver.common.by import By
from pages.base_page import Page


class PDP(Page):
    ADD_TO_BAG = (By.CSS_SELECTOR, '.add-to-cart-btn')
    SIZES_CLICKABLE = (By.CSS_SELECTOR, '.css-xf3ahq')
    SIZES = (By.XPATH, '//input[@name="skuAndSize"]')
    CART_BTN = (By.ID, 'nav-cart')
    CART_MODAL = (By.CSS_SELECTOR, '.AddToCartSuccessHeader')


    def select_size(self):
        sizes = self.find_elements(*self.SIZES)
        clickable_sizes = self.find_elements(*self.SIZES_CLICKABLE)
        # print(sizes)
        for i in range(len(sizes)):
            # print(sizes[i].is_enabled())
            if sizes[i].is_enabled():
                clickable_sizes[i].click()
                break

    def add_to_bag(self):
        self.driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
        # self.driver.implicitly_wait(1)
        self.wait_for_clickable_element(*self.ADD_TO_BAG)
        self.click(*self.ADD_TO_BAG)


    def go_to_cart(self):
        self.wait_for_element_appear(*self.CART_MODAL)
        self.click(*self.CART_BTN)