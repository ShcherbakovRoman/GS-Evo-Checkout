from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.select import Select
from time import sleep
from random import randint


class Evo_Checkout(Page):
    BECOME_MEMBER_BTN = (By.XPATH, '//button[@data-ref="checkout.sign-up-btn"]')
    LOGIN_BTN = (By.XPATH, '//button[@data-ref="checkout.login-btn"]')
    NAME = (By.ID, 'firstName')
    LAST_NAME = (By.ID, 'lastName')
    MIDDLE_NAME = (By.ID, 'middleName')
    ADDY_LINE_1 = (By.ID, 'addressLine1')
    ADDY_LINE_2 = (By.ID, 'addressLine2')
    POSTAL_CODE = (By.ID, 'postalCode')
    CITY = (By.ID, 'city')
    EMAIL = (By.ID, 'emailAddress')
    PHONE_NUMBER = (By.XPATH, '//input[@placeholder="Phone Number"]')
    MX_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="Número de teléfono"]')
    TR_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="Telefon Numarası"]')
    RU_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="Номер телефона"]')
    TW_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="電話號碼"]')
    TH_PHONE_NUMBER = (By.XPATH, '//input[@placeholder="หมายเลขโทรศัพท์"]')
    CONSENT_BOX = (By.CSS_SELECTOR, '.input-checkbox__container')
    EVO_CONTINUE_BTN = (By.CSS_SELECTOR, '.btn.btn--primary')
    EXPRESS_SHIPPING = (By.CSS_SELECTOR, 'esw-toggle-option:last-child')
    CARD_NAME = (By.ID, 'cardName-input')
    CARD_NUMBER = (By.ID, 'cardNumber-input')
    CARD_EXP = (By.ID, 'cardExpiry-input')
    CVV = (By.ID, 'cardCvc-input')
    PLACE_ORDER_BTN = (By.ID, 'new-card-paynow')
    PAYMENT_OPTION_BTN = (By.CSS_SELECTOR, '.payment-method-button')
    PAYMENT_FRAME = (By.ID, 'paymentsIframe')
    ORDER_CONFIRMATION = (By.CSS_SELECTOR, '.confirmation__summary-sections-title')
    QUANTITY = (By.CSS_SELECTOR, '.cart-item__info')
    ITEMS_IN_CART = (By.XPATH, '//esw-cart-item[@class]')
    MEMBER_EMAIL_ENTRY = (By.XPATH, '//input[@name="emailAddress"]')
    MEMBER_PW_ENTRY = (By.XPATH, '//input[@name="password"]')
    MEMBER_FIRSTNAME_ENTRY = (By.XPATH, '//input[@name="firstName"]')
    MEMBER_LASTNAME_ENTRY = (By.XPATH, '//input[@name="lastName"]')
    MEMBER_DOB_ENTRY = (By.XPATH, '//input[@name="dateOfBirth"]')
    COUNTRY_LIST = (By.XPATH, '//select[@name="country"]')
    GENDER_BTN = (By.XPATH, '//li[@class=""]')
    JOIN_US_CTA = (By.CSS_SELECTOR, '.joinSubmit')
    LOGIN_CTA = (By.CSS_SELECTOR, '.loginSubmit')
    HEADER_LOGIN_BTN = (By.XPATH, '//button[@aria-label="Login"]')
    HEADER_BTNS = (By.CSS_SELECTOR, '.fs-8.ml-10')
    LOGIN_MODAL = (By.ID, 'nike-unite-login-view')
    SAVED_ADDRESS = (By.CSS_SELECTOR, '.saved-addresses__toggle-content')
    DELETE_CC_BTN = (By.ID, 'stored-cards-button-delete')
    EDD_SIDE_PANEL = (By.CSS_SELECTOR, '.shipment__title')
    EDD_CENTRAL_PANEL = (By.CSS_SELECTOR, '.date')
    EDD_SPEED_SELECTOR = (By.CSS_SELECTOR, '.shipping__date')
    STORED_CARD_LIST = (By.ID, 'stored-cards-list-select')
    SHIPPING_SPEED_BTN = (By.CSS_SELECTOR, '.shipping__service-level')
    BILLING_CHECKBOX = (By.CSS_SELECTOR, '.checkmark')
    SUBTOTAL = (By.CSS_SELECTOR, 'div.price-summary__price')
    NATID = (By.ID, 'simpleId')
    TW_NATID = (By.ID, 'passportNumber')
    SMSCODE_FIELD = (By.ID, 'smsCode')
    SUBMIT_SMS = (By.ID, 'submitBtn')
    STATE = (By.ID, 'region')
    UAE_AREA = (By.ID, 'city')
    IN_SUCCESS_PAY = (By.CSS_SELECTOR, '.success')
    PH_DISTRICT = (By.ID, 'addressLine3')
    TW_PAY_CONSENT = (By.CSS_SELECTOR, '.checkmark')


    tw_firstname = '名字'
    tw_lastname = "姓氏"
    name = 'Roman'
    middlename = 'Aleksandrovich'
    lastname = 'Shcherbakov'
    address_line1 = 'Test Address line 1'
    address_line2 = 'Test Address line 2'
    ru_city = 'Краснодар'
    canada_postal_code = 'K2G 4A1'
    au_postal_code = '2345'
    sg_postal_code = '234567'
    mx_postal_code = '72420'
    tr_postal_code = '23456'
    ru_postal_code = '350000'
    il_postal_code = '1234567'
    ro_postal_code = '123456'
    sa_postal_code = '12345'
    bg_postal_code = '1234'
    sk_postal_code = '12345'
    hr_postal_code = '23456'
    vn_postal_code = '12345'
    in_postal_code = '234567'
    ma_postal_code = '12345'
    ph_postal_code = '1234'
    id_postal_code = '12345'
    tw_postal_code = '12345'
    th_postal_code = '12345'
    ph_region = 'Aurora'
    ph_district = 'Dibalo'
    city = 'TestCity'
    il_city = 'Jerusalem'
    sa_city = 'Baha'
    ph_city = 'San Luis'
    email = 'test@test.com'
    universal_phone_number = '9712233445'
    au_phone_number = '234235234'
    sg_phone_number = '97122334'
    tr_phone_number = '3789012345'
    il_phone_number = '97122334'
    tr_natid = '23456789011'
    ch_phone_number = '971223344'
    no_phone_number = '97122334'
    za_phone_number = '971223344'
    ro_phone_number = '234567'
    uae_phone_number = '97122334'
    sa_phone_number = '567890123'
    bg_phone_number = '9712233'
    sk_phone_number = '971223344'
    hr_phone_number = '971223344'
    vn_phone_number = '971223344'
    ma_phone_number = '97122334'
    tw_phone_number = '971223344'
    th_phone_number = '971223344'
    za_natid = '1234567890123'
    il_natid = '123456789'
    sa_natid = '1234567890'
    in_natid = 'atest1234o'
    tw_natid = 'f342324242'

    confirmation_numbers = []

    def verify_evo_checkout(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)

    def enter_ship_details(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.canada_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_au(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_sg(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sg_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.sg_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_mx(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.mx_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.MX_PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_tr(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.tr_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.tr_phone_number, *self.TR_PHONE_NUMBER)
        self.input_text(Evo_Checkout.tr_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_ru(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.middlename, *self.MIDDLE_NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ru_city, *self.CITY)
        self.input_text(Evo_Checkout.ru_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.RU_PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_ch(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.ch_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_no(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.no_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_nz(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_za(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.za_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.za_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_il(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.il_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.il_city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.il_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.il_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_ro(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ro_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.ro_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_uae(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        dd_emirates = self.find_element(*self.STATE)
        select1 = Select(dd_emirates)
        select1.select_by_value('2: Object')
        self.driver.find_element_by_xpath("//body").click() # click anywhere on blank
        dd_area = self.find_element(*self.UAE_AREA)
        select2 = Select(dd_area)
        select2.select_by_visible_text('Dubai')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.uae_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_sa(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sa_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.sa_city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.sa_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.sa_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_bg(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.bg_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.bg_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_sk(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sk_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.sk_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_hr(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.hr_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.hr_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_vn(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.vn_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_province = self.find_element(*self.STATE)
        select = Select(dd_province)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.vn_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_in(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.in_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.in_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_ma(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ma_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.ma_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_ph(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ph_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.ph_city, *self.CITY)
        self.input_text(Evo_Checkout.ph_region, *self.STATE)
        self.input_text(Evo_Checkout.ph_district, *self.PH_DISTRICT)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_id(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.id_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_tw(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.tw_lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.tw_firstname, *self.NAME)
        self.input_text(Evo_Checkout.tw_postal_code, *self.POSTAL_CODE)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.tw_phone_number, *self.TW_PHONE_NUMBER)
        self.input_text(Evo_Checkout.tw_natid, *self.TW_NATID)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_ship_details_th(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.th_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        self.input_text(Evo_Checkout.th_phone_number, *self.TH_PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def select_shipping_method(self, ship_method):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        if ship_method == "Standard":
            self.click(*self.EVO_CONTINUE_BTN)
        else:
            self.click(*self.EXPRESS_SHIPPING)
            sleep(1)
            self.click(*self.EVO_CONTINUE_BTN)

    def confirm_billing(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_payment(self):
        self.wait_for_element_appear(*self.PAYMENT_FRAME)
        self.driver.switch_to.frame('paymentsIframe')
        self.driver.switch_to.frame('new-card-iframe')
        self.wait_for_element_appear(*self.CARD_NAME)
        self.input_text('Roman Shch', *self.CARD_NAME)
        self.input_text('4111111111111111', *self.CARD_NUMBER)
        self.input_text('0824', *self.CARD_EXP)
        self.input_text('824', *self.CVV)
        self.driver.switch_to.default_content()

    def enter_tr_payment(self):
        self.wait_for_element_appear(*self.PAYMENT_FRAME)
        self.driver.switch_to.frame('paymentsIframe')
        self.driver.switch_to.frame('new-card-iframe')
        self.wait_for_element_appear(*self.CARD_NAME)
        self.input_text('Roman Shch', *self.CARD_NAME)
        self.input_text('9792020000000001', *self.CARD_NUMBER)
        self.input_text('0824', *self.CARD_EXP)
        self.input_text('824', *self.CVV)
        self.driver.switch_to.default_content()

    def check_pay_consent(self):
        self.driver.switch_to.frame('paymentsIframe')
        self.driver.switch_to.frame('new-card-iframe')
        self.click(*self.TW_PAY_CONSENT)


    def submit_order(self):
        self.driver.switch_to.frame('paymentsIframe')
        self.wait_for_clickable_element(*self.PLACE_ORDER_BTN)
        self.click(*self.PLACE_ORDER_BTN)
        self.driver.switch_to.default_content()

    def confirm_success_pmnt(self):
        self.wait_for_element_appear(*self.IN_SUCCESS_PAY)
        self.click(*self.IN_SUCCESS_PAY)

    # def submit_sms_code(self):
    #     self.driver.switch_to.frame('paymentsIframe')
    #     self.driver.switch_to.frame('new-card-iframe')
    #     self.wait_for_element_appear(*self.SUBMIT_SMS)
    #     self.input_text('283126', *self.SMSCODE_FIELD)
    #     self.click(*self.SUBMIT_SMS)

    def order_confirmation_page(self):
        self.wait_for_element_appear(*self.ORDER_CONFIRMATION)
        order_conf_number = self.find_element(*self.ORDER_CONFIRMATION).text
        print(order_conf_number)
        order_number = ''
        for char in order_conf_number:
            if char.isdigit():
                order_number += char
        order_number = "ESW" + order_number
        print(order_number)
        Evo_Checkout.confirmation_numbers.append(order_number)
        print(Evo_Checkout.confirmation_numbers)

    def verify_qty_in_checkout(self, product_qty):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        quantity = str(self.find_element(*self.QUANTITY).text)
        assert quantity[-1] == str(product_qty), f'Error. Expected {product_qty} does not match actual {quantity[-1]}'

    def verify_qty_in_confirmation(self, product_qty):
        quantity = self.find_element(*self.QUANTITY).text
        assert quantity[-1] == product_qty, f'Error. Expected {product_qty} does not match actual {quantity[-1]}'

    def verify_number_of_product_lines(self, line_qty):
        number_of_lines = len(self.find_elements(*self.ITEMS_IN_CART))
        assert str(number_of_lines) == line_qty, f'Error. Expect {line_qty}, but got {number_of_lines}'

    def verify_submit_button(self):
        self.driver.switch_to.frame('paymentsIframe')
        self.wait_for_clickable_element(*self.PLACE_ORDER_BTN)
        submit_button = self.find_element(*self.PLACE_ORDER_BTN)
        assert submit_button.is_enabled() == True, f'Error. Submit Button is inactive'

    def become_member_cta(self):
        self.wait_for_element_appear(*self.BECOME_MEMBER_BTN)
        self.click(*self.BECOME_MEMBER_BTN)

    def new_member_details(self):
        random_number = randint(0, 1000)
        global email, pw
        email = f'autotest{random_number}@roman.com'
        pw = f'Autotest{random_number}'
        self.input_text(email, *self.MEMBER_EMAIL_ENTRY)
        self.input_text(pw, *self.MEMBER_PW_ENTRY)
        self.input_text('Roman', *self.MEMBER_FIRSTNAME_ENTRY)
        self.input_text('Shcherbakov', *self.MEMBER_LASTNAME_ENTRY)
        self.input_text('10141988', *self.MEMBER_DOB_ENTRY)
        self.click(*self.GENDER_BTN)
        self.click(*self.JOIN_US_CTA)

    def click_login(self):
        self.wait_for_element_appear(*self.LOGIN_BTN)
        self.click(*self.LOGIN_BTN)

    def enter_login_info(self):
        email = 'test1@roman.com'
        pw = 'Test0test'
        print(email, pw)
        self.input_text(email, *self.MEMBER_EMAIL_ENTRY)
        self.input_text(pw, *self.MEMBER_PW_ENTRY)
        self.click(*self.LOGIN_CTA)

    def verify_loggedin_state(self):
        self.wait = WebDriverWait(self, 10)
        self.wait.until(EC.invisibility_of_element_located((self.LOGIN_CTA)))
        header_buttons = self.find_elements(*self.HEADER_BTNS)
        print(len(header_buttons))
        assert len(header_buttons) == 2, f'User is not logged in'

    def verify_loggedin_state_tr(self):
        self.wait = WebDriverWait(self, 10)
        self.wait.until(EC.invisibility_of_element_located((self.LOGIN_CTA)))
        header_buttons = self.find_elements(*self.HEADER_BTNS)
        assert len(header_buttons) == 1, f'User is not logged in'

    def enter_member_w_address_info(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text('test1@roman.com', *self.MEMBER_EMAIL_ENTRY)
        self.input_text('Test0test', *self.MEMBER_PW_ENTRY)
        self.click(*self.LOGIN_CTA)
        sleep(5)

    def verify_saved_address_present(self):
        self.wait_for_element_appear(*self.SAVED_ADDRESS)

    def click_continue(self):
        self.click(*self.EVO_CONTINUE_BTN)

    def verify_saved_cc_present(self):
        self.wait_for_element_appear(*self.PAYMENT_FRAME)
        self.driver.switch_to.frame('paymentsIframe')
        self.wait_for_element_appear(*self.STORED_CARD_LIST)
        self.click(*self.DELETE_CC_BTN)

    def compare_edds(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        edd2 = self.find_element(*self.EDD_SIDE_PANEL).text
        edd3 = self.find_element(*self.EDD_CENTRAL_PANEL).text
        edd1 = self.find_element(*self.EDD_SPEED_SELECTOR).text
        assert edd1 == edd2 == edd3, f'EDDs are not matching: {edd1}, {edd2}, {edd3}'

    def enter_invalid_ship_details(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text('Roman', *self.NAME)
        self.input_text('Shch', *self.LAST_NAME)
        self.input_text('Test Address line 1', *self.ADDY_LINE_1)
        self.input_text('Test Address line 2', *self.ADDY_LINE_2)
        self.input_text('K2G 4A1', *self.POSTAL_CODE)
        self.input_text('TestCity', *self.CITY)
        self.input_text('test@test.com', *self.EMAIL)
        # self.input_text('9712233445', *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_au(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_sg(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sg_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.sg_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_mx(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.mx_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_tr(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.tr_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.tr_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.tr_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_ru(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.middlename, *self.MIDDLE_NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ru_city, *self.CITY)
        self.input_text(Evo_Checkout.ru_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.universal_phone_number, *self.RU_PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_ch(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_no(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_nz(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_za(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.au_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.za_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_il(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.il_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.il_city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.il_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.il_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_ro(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ro_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.ro_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)


    def enter_invalid_ship_details_uae(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        dd_emirates = self.find_element(*self.STATE)
        select1 = Select(dd_emirates)
        select1.select_by_value('2: Object')
        self.driver.find_element_by_xpath("//body").click() # click anywhere on blank
        dd_area = self.find_element(*self.UAE_AREA)
        select2 = Select(dd_area)
        select2.select_by_visible_text('Dubai')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.uae_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_sa(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sa_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.sa_city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.sa_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.sa_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_bg(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.bg_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.bg_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_sk(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.sk_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.sk_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_hr(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.hr_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.sk_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_vn(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.vn_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_province = self.find_element(*self.STATE)
        select = Select(dd_province)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.vn_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)
        self.click(*self.EVO_CONTINUE_BTN)

    def enter_invalid_ship_details_in(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.in_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.input_text(Evo_Checkout.in_natid, *self.NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_ma(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ma_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.ma_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_ph(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.ph_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.ph_city, *self.CITY)
        self.input_text(Evo_Checkout.ph_region, *self.STATE)
        self.input_text(Evo_Checkout.ph_district, *self.PH_DISTRICT)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_id(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.id_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_tw(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.tw_lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.tw_firstname, *self.NAME)
        self.input_text(Evo_Checkout.tw_postal_code, *self.POSTAL_CODE)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.city, *self.CITY)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.tw_phone_number, *self.TW_PHONE_NUMBER)
        self.input_text(Evo_Checkout.tw_natid, *self.TW_NATID)
        self.click(*self.CONSENT_BOX)

    def enter_invalid_ship_details_th(self):
        self.wait_for_element_appear(*self.EVO_CONTINUE_BTN)
        self.input_text(Evo_Checkout.name, *self.NAME)
        self.input_text(Evo_Checkout.lastname, *self.LAST_NAME)
        self.input_text(Evo_Checkout.address_line1, *self.ADDY_LINE_1)
        self.input_text(Evo_Checkout.address_line2, *self.ADDY_LINE_2)
        self.input_text(Evo_Checkout.city, *self.CITY)
        dd_state = self.find_element(*self.STATE)
        select = Select(dd_state)
        select.select_by_value('2: Object')
        self.input_text(Evo_Checkout.th_postal_code, *self.POSTAL_CODE)
        self.input_text(Evo_Checkout.email, *self.EMAIL)
        # self.input_text(Evo_Checkout.th_phone_number, *self.TW_PHONE_NUMBER)
        self.click(*self.CONSENT_BOX)

    def verify_continue_btn_inactive(self):
        continue_btn = self.find_element(*self.EVO_CONTINUE_BTN)
        assert continue_btn.is_enabled() == False, f'Continue button is enabled'

    def add_missing_ship_info(self):
        self.input_text('9712233445', *self.PHONE_NUMBER)

    def add_missing_ship_info_au(self):
        self.input_text(Evo_Checkout.au_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_sg(self):
        self.input_text(Evo_Checkout.sg_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_mx(self):
        self.input_text(Evo_Checkout.universal_phone_number, *self.MX_PHONE_NUMBER)

    def add_missing_ship_info_tr(self):
        self.input_text(Evo_Checkout.tr_phone_number, *self.TR_PHONE_NUMBER)

    def add_missing_ship_info_ru(self):
        self.input_text(Evo_Checkout.universal_phone_number, *self.RU_PHONE_NUMBER)

    def add_missing_ship_info_ch(self):
        self.input_text(Evo_Checkout.ch_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_no(self):
        self.input_text(Evo_Checkout.no_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_za(self):
        self.input_text(Evo_Checkout.za_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_il(self):
        self.input_text(Evo_Checkout.il_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_ro(self):
        self.input_text(Evo_Checkout.ro_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_uae(self):
        self.input_text(Evo_Checkout.uae_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_sa(self):
        self.input_text(Evo_Checkout.sa_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_bg(self):
        self.input_text(Evo_Checkout.bg_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_sk(self):
        self.input_text(Evo_Checkout.sk_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_hr(self):
        self.input_text(Evo_Checkout.hr_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_vn(self):
        self.input_text(Evo_Checkout.vn_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_in(self):
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_ma(self):
        self.input_text(Evo_Checkout.ma_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_ph(self):
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_id(self):
        self.input_text(Evo_Checkout.universal_phone_number, *self.PHONE_NUMBER)

    def add_missing_ship_info_tw(self):
        self.input_text(Evo_Checkout.tw_phone_number, *self.TW_PHONE_NUMBER)

    def add_missing_ship_info_th(self):
        self.input_text(Evo_Checkout.th_phone_number, *self.TH_PHONE_NUMBER)

    def verify_shipping_speed_page(self):
        self.find_element(*self.SHIPPING_SPEED_BTN)

    def verify_continue_btn_clickable(self):
        continue_btn = self.find_element(*self.EVO_CONTINUE_BTN)
        assert continue_btn.is_enabled() == True, 'Continue button is disabled'

    def click_billing_checkbox(self):
        self.click(*self.BILLING_CHECKBOX)

    def compare_billing_shipping_details(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.PHONE_NUMBER).get_attribute('value')
        billing_phone_nospaces = billing_phone_number.replace(' ', '')
        billing_phone_nosymbols = billing_phone_nospaces.replace('+', '')
        len_dif = len(billing_phone_nosymbols) - len(Evo_Checkout.universal_phone_number)
        clean_billing_phone = billing_phone_nosymbols[len_dif:]

        assert billing_name == Evo_Checkout.name, f'Error. Expected {Evo_Checkout.name} does not match actual {billing_name}'
        assert billing_lastname == Evo_Checkout.lastname, f'Error. Expected {Evo_Checkout.lastname} does not match actual {billing_lastname}'
        assert billing_addy1 == Evo_Checkout.address_line1, f'Error. Expected {Evo_Checkout.address_line1} does not match actual {billing_addy1}'
        assert billing_addy2 == Evo_Checkout.address_line2, f'Error. Expected {Evo_Checkout.address_line2} does not match actual {billing_addy2}'
        assert billing_postal_code == Evo_Checkout.canada_postal_code, f'Error. Expected {Evo_Checkout.canada_postal_code} does not match actual {billing_postal_code}'
        assert clean_billing_phone == Evo_Checkout.universal_phone_number, f'Error. Expected {Evo_Checkout.universal_phone_number} does not match actual {clean_billing_phone}'

    def verify_billing_empty(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_addy2 == '', f'Error. Expected empty field does not match actual {billing_addy2}'
        assert billing_postal_code == '', f'Error. Expected empty field does not match actual {billing_postal_code}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_billing_empty_tr(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.TR_PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_postal_code == '', f'Error. Expected empty field does not match actual {billing_postal_code}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_billing_empty_mx(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.MX_PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_addy2 == '', f'Error. Expected empty field does not match actual {billing_addy2}'
        assert billing_postal_code == '', f'Error. Expected empty field does not match actual {billing_postal_code}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_billing_empty_ru(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_middlename = self.find_element(*self.MIDDLE_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.RU_PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_middlename == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_addy2 == '', f'Error. Expected empty field does not match actual {billing_addy2}'
        assert billing_postal_code == '', f'Error. Expected empty field does not match actual {billing_postal_code}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_billing_empty_uae(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_phone_number = self.find_element(*self.PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_addy2 == '', f'Error. Expected empty field does not match actual {billing_addy2}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_billing_empty_th(self):
        billing_name = self.find_element(*self.NAME).get_attribute('value')
        billing_lastname = self.find_element(*self.LAST_NAME).get_attribute('value')
        billing_addy1 = self.find_element(*self.ADDY_LINE_1).get_attribute('value')
        billing_addy2 = self.find_element(*self.ADDY_LINE_2).get_attribute('value')
        billing_postal_code = self.find_element(*self.POSTAL_CODE).get_attribute('value')
        billing_phone_number = self.find_element(*self.TH_PHONE_NUMBER).get_attribute('value')

        assert billing_name == '', f'Error. Expected empty field does not match actual {billing_name}'
        assert billing_lastname == '', f'Error. Expected empty field does not match actual {billing_lastname}'
        assert billing_addy1 == '', f'Error. Expected empty field does not match actual {billing_addy1}'
        assert billing_addy2 == '', f'Error. Expected empty field does not match actual {billing_addy2}'
        assert billing_postal_code == '', f'Error. Expected empty field does not match actual {billing_postal_code}'
        assert billing_phone_number == '', f'Error. Expected empty field does not match actual {billing_postal_code}'

    def verify_calculations(self):
        sleep(10)
        subtotal_values = self.find_elements(*self.SUBTOTAL)
        sub_values_int = []
        for value in subtotal_values:
            sub_values_int.append(value.text)
        # print(sub_values_int)
        temp_list = []
        for price in sub_values_int:
            if ',' in price:
                price = price.replace(',', '.')
            for char in price:
                if char not in '1234567890.':
                    price = price.replace(char, '')
            temp_list.append(price)
        sub_values_int = temp_list
        grand_total = sub_values_int[-1]
        grand_total = float(grand_total)
        sub_values_int = sub_values_int[0:-1]
        final_list = []
        for value in sub_values_int:
            final_list.append(float(value))
        assert sum(final_list) == grand_total, f'Error. The calculations are incorrect. Grand Total is {grand_total} and sum of all values is {sum(final_list)}'

    def verify_calculations_bn(self):
        sleep(8)
        subtotal_values = self.find_elements(*self.SUBTOTAL)
        sub_values_int = []
        for value in subtotal_values:
            sub_values_int.append(value.text)
        temp_list = []
        for price in sub_values_int:
            for char in price:
                if char not in '1234567890':
                    price = price.replace(char, '')
            temp_list.append(price)
        sub_values_int = temp_list
        grand_total = int(sub_values_int[-1])
        sub_values_int = sub_values_int[0:-1]
        final_list = []
        for value in sub_values_int:
            final_list.append(int(value))
        assert sum(final_list) == grand_total, f'Error. The calculations are incorrect. Grand Total is {grand_total} and sum of all values is {sum(final_list)}'




