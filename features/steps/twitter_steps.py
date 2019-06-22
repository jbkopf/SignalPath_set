from behave import step
from nose.tools import assert_in


@step('I go to twitter')
def go_to_twitter(context):
    context.driver.get('https://www.twitter.com')
    url = context.driver.current_url
    assert_in('twitter', url, 'twitter not found in current url')