from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from behave import fixture, use_fixture


@fixture
def initialize_browser(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1400,900')
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    yield context.driver
    # -- CLEANUP-FIXTURE PART:
    context.driver.quit()

def before_all(context):
    use_fixture(initialize_browser, context)