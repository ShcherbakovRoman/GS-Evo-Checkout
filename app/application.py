from pages.esw_harness import eSWHarness
from pages.evo_checkout import Evo_Checkout
from pages.home_page import HomePage
from pages.pw import PW
from pages.pdp import PDP
from pages.cart import Cart
from pages.esw_csp_sit76 import CSP_sit76


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.esw_harness = eSWHarness(self.driver)
        self.evo_checkout = Evo_Checkout(self.driver)
        self.home_page = HomePage(self.driver)
        self.pw = PW(self.driver)
        self.pdp = PDP(self.driver)
        self.cart = Cart(self.driver)
        self.esw_csp_sit76 = CSP_sit76(self.driver)

