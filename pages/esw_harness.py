from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.select import Select


class eSWHarness(Page):
    LOGIN_FIELD = (By.ID, 'UserEmail')
    PW_FIELD = (By.ID, 'UserPass')
    LOGIN_BTN = (By.ID, 'Submit1')
    TARGET_URL = (By.ID, 'targetURL')
    TARGET_JSON = (By.ID, 'JsonFiles')
    COUNTRY_LIST = (By.ID, 'CountryCode')
    SUBMIT_BTN = (By.ID, 'qaTestSubmit')
    country_codes = {
        'Australia': 'AU',
        'Bulgaria': 'BG',
        'Canada': 'CA',
        'Chile': 'CL',
        'Croatia': 'HR',
        'Egypt': 'EG',
        'Indonesia': 'ID',
        'India': 'IN',
        'Israel': 'IL',
        'Malaysia': 'MY',
        'Mexico': 'MX',
        'Morocco': 'MA',
        'New Zealand': 'NZ',
        'Norway': 'NO',
        'Philippines': 'PH',
        'Puerto Rico': 'PR',
        'Romania': 'RO',
        'Russia': 'RU',
        'Saudi Arabia': 'SA',
        'Singapore': 'SG',
        'Slovakia': 'SK',
        'South Africa': 'ZA',
        'Switzerland': 'CH',
        'Turkey': 'TR',
        'Thailand': 'TH',
        'Taiwan': 'TW',
        'UAE': 'AE',
        'Vietnam': 'VN'
    }
    EVO_CONTINUE_BTN = (By.CSS_SELECTOR, '.btn.btn--primary')
    PRODUCT_QTY = (By.ID, '10621931_Quantity')
    PRODUCT_PRICE = (By.ID, '10621931_Price')
    LANGUAGE_LIST = (By.ID, 'LanguageCode')

    def enter_harness(self, user, pw):
        self.open_page('http://dev-testharness.nike.eshopworld.net/logon.aspx?ReturnUrl=%2fQATesting%2fNikePreOrder')
        self.input_text(user, *self.LOGIN_FIELD)
        self.input_text(pw, *self.PW_FIELD)
        self.click(*self.LOGIN_BTN)

    def select_endpoint(self, endpoint):
        self.wait_for_element_appear(*self.TARGET_URL)
        dd_env = self.find_element(*self.TARGET_URL)
        select = Select(dd_env)
        if endpoint == 'SIT76':
            value = 'SIT76'
        elif endpoint == 'SIT75':
            value = 'PreProd'
        select.select_by_value(value)

    def select_json(self, line_qty, merch_group):
        if line_qty == '1':
            if merch_group == 'XP':
                value = '2'
            else:
                value = '1'
        elif line_qty == '2':
            if merch_group == 'XP':
                value = '4'
            else:
                value = '3'
        elif line_qty == '3':
            if merch_group == 'XP':
                value = '6'
            else:
                value = '5'
        elif line_qty == '4':
            value = '7'
        elif line_qty == '5':
            value = '8'
        dd_json = self.find_element(*self.TARGET_JSON)
        select = Select(dd_json)
        select.select_by_value(value)

    def select_country(self, country):
        self.wait_for_element_appear(*self.COUNTRY_LIST)
        dd_country = self.find_element(*self.COUNTRY_LIST)
        select = Select(dd_country)
        value = eSWHarness.country_codes.get(country, "Country Error")
        select.select_by_value(value)


    def select_language(self):
        self.wait_for_element_appear(*self.LANGUAGE_LIST)
        dd_language = self.find_element(*self.LANGUAGE_LIST)
        select = Select(dd_language)
        # language = 'enGB'
        select.select_by_value('enGB')

    def select_product_qty(self, product_qty):
        qty_fields = self.find_elements(*self.PRODUCT_QTY)
        # print(qty_fields)
        for field in qty_fields:
            field.clear()
            field.send_keys(product_qty)
            product_qty = str((int(product_qty) + 1))

    def change_price(self):
        self.clear_field(*self.PRODUCT_PRICE)
        self.input_text('50', *self.PRODUCT_PRICE)

    def submit_payload(self):
        self.click(*self.SUBMIT_BTN)
