from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from pages.esw_harness import eSWHarness


class HomePage(Page):
    MEN_PRODUCTS = (By.CSS_SELECTOR, '[data-path=men]')
    FOOTBALL_PRODUCTS = (By.CSS_SELECTOR, '[data-path="men:shoes:soccer football"]')
    JORDAN_PRODUCTS = (By.CSS_SELECTOR, '[data-path="men:shoes:jordan"]')
    CLOSE_LOCATION_MSG = (By.CSS_SELECTOR, '.hf-geomismatch-btn-close')

    def open_home_page(self, country):
        value = eSWHarness.country_codes.get(country, "Country Error").lower()
        self.open_page(f'https://www.nike.com/{value}')

    def hover_over_menu(self):
        men_menu = self.find_element(*self.MEN_PRODUCTS)
        actions = ActionChains(self.driver)
        actions.move_to_element(men_menu).perform()

    def select_from_menu(self):
        self.click(*self.JORDAN_PRODUCTS)

    def confirm_location(self):
        self.click(*self.CLOSE_LOCATION_MSG)



