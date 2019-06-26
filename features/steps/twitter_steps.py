from behave import step
from nose.tools import assert_in,assert_not_in
from features.environment import initialize_browser
from time import sleep
from math import ceil


@step('I go to (.*)')
def go_to_url(context, url):
    context.driver.get(url)
    current_url = context.driver.current_url
    sleep(5)
    assert_in('twitter', current_url, 'twitter not found in current url')

@step('I login to twitter setting remember me to (yes|no)')
def login_to_twitter(context, remember):
    # context.driver.find_element_by_class_name('StaticLoggedOutHomePage-buttonLogin').click()
    # context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/fieldset/div[1]/input').send_keys('jkopftest')
    context.driver.find_element_by_class_name("js-username-field").send_keys('jkopftest')
    context.driver.find_element_by_class_name("js-password-field").send_keys('P@ssw0rd')
    if remember == "no":
        if context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input').is_selected():
            context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input').click()
    elif remember == "yes":
        if not context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input').is_selected():
            context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/div/label/input').click()

    context.driver.find_element_by_xpath('//*[@id="page-container"]/div/div[1]/form/div[2]/button').click()
    context.user_cookies = context.driver.get_cookies()
    assert_in('JKopf', context.driver.page_source)

@step('I reset the browser for twitter')
def reset_browser_twitter(context):
    context.driver.close()
    initialize_browser(context)
    # necessary to access page on same domain before setting cookies
    context.driver.get("https://twitter.com/account/suspended")

@step('I see I (am not|am) logged in')
def check_loged_in(context, logged_in):
    if logged_in == "am not":
        assert_not_in("JKopf", context.driver.page_source)
    else:
        assert_in("JKopf",context.driver.page_source)

@step('I go with cookies to (.*)')
def go_to_url_with_cookies(context, url):
    # opens page using cookies from previous session

    for cookie in context.user_cookies:
        if "expiry" in cookie:
            cookie["expiry"] = int(ceil(cookie["expiry"]))
            del cookie["domain"]  # removes misformated domains, default current domain is used
            context.driver.add_cookie(cookie)

    context.driver.get(url)

