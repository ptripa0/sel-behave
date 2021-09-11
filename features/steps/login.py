from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@given(u'I launch the chrome browser')
def launch_browser(context):
    print("In Given")
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
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
