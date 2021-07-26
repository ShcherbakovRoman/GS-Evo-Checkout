from selenium import webdriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from app.application import Application

bs_user = 'romanshcherbakov1'
bs_key = 'VM3JVhSezDihBGmz6izr'

def browser_init(context, name):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(executable_path='/Users/rshche/Automation/chromedriver')
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    ### for BrowserStack ###
    # desired_cap = {
    #     'browser': 'Chrome',
    #     'browser_version': '84.0',
    #     'os': 'Windows',
    #     'os_version': '10',
    #     'name': name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    ### for logger ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(executable_path='/Users/rshche/Automation/chromedriver'), MyListener())


    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # logger.info(f'\nStarted scenario: {scenario.name}')
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
    # logger.info(f'\nStarted step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        # logger.info(f'\nStep failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
