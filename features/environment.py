from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from utilities.configuration import *
from utilities.locator_resources import *


# Before a feature file
def before_feature(context, feature):
    context.is_logged_in = False


# Before each scenario
def before_scenario(context, scenario):
    context.chrome_options = Options()
    context.chrome_options.add_argument("--headless")
    # context.chrome_options.add_argument("--window-size=1920x1080")
    context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=context.chrome_options)
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(get_config()['Application']['url'])

    context.driver.find_element_by_xpath(locator_resources.signup_button_xpath).click()
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_id("email").send_keys(get_config()['User']['username'])
    context.driver.find_element_by_id("password").send_keys(get_config()['User']['password'])
    context.driver.find_element_by_xpath(locator_resources.login_button_xpath).click()
    context.is_logged_in = True


# after each scenario
def after_scenario(context, scenario):
    if context.is_logged_in is True:
        context.driver.find_element_by_xpath(locator_resources.settings_button_xpath).click()
        context.driver.find_element_by_css_selector(locator_resources.logout_button_css).click()
        context.driver.quit()
        context.is_logged_in = False

# Tear down - Delete the project
# def after_feature(context, feature):
#    if context.is_logged_in is True:
#        context.driver.find_element_by_css_selector("input[placeholder='Search...']").send_keys(project_name)
#        context.driver.find_element_by_xpath(
#            "//i[@class='button__icon icon--cog']//div[@class='svg-icon ']//*[local-name()='svg']").click()
#        context.driver.find_element_by_xpath("//p[contains(text(),'Delete')]").click()
#        context.driver.find_element_by_css_selector(
#            "button[class='button button--accent'] span[class='button__label']").click()
#        context.is_logged_in = False
