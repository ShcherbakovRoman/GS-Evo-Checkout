from selenium.webdriver.common.by import By
from pages.base_page import Page


class PW(Page):
    product_number = '7'
    PRODUCT = (By.XPATH, '//div[@data-product-position="' + product_number + '"]')
    INVALID_PRODUCT = (By.CSS_SELECTOR, ".product-card__messaging.accent--color")
    ALL_PRODUCTS = (By.CSS_SELECTOR, ".product-card")


    def select_product(self):
        product_number = 7
        products_on_page = len(self.find_elements(*self.ALL_PRODUCTS))
        while product_number != products_on_page:
                product = self.find_element(*self.PRODUCT)
                invalid_product = self.find_element(*self.INVALID_PRODUCT)
                if invalid_product == product:
                    product_number += 1
                else:
                    self.click(*self.PRODUCT)
                    break

