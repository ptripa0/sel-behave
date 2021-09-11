from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@given(u'I launch the chrome browser')
def launch_browser(context):
    print("In Given")
    # instantiate a chrome options object so you can set the size and headless preference
    context.chrome_options = Options()
    context.chrome_options.add_argument("--headless")
    context.chrome_options.add_argument("--window-size=1920x1080")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=context.chrome_options)
    context.driver.get("https://opensource-demo.orangehrmlive.com/")
    assert True


@then(u'Enter username and password')
def step_impl(context):
    logo = context.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[3]/div[1]/img[1]").is_displayed()
    assert logo is True
    #context.driver.find_element_by_xpath("//input[@id='txtUsername']").is_displayed()



@then(u'Click on login button')
def step_impl(context):
    assert context.failed is False


@then(u'User must successfully logged in to the D3A.io application')
def step_impl(context):
    assert context.failed is False


@then(u'Landing page must be visible')
def step_impl(context):
    assert context.failed is False
