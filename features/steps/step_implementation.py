from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

expectedUrl = "https://www.d3a.io/"


@given(u'User launches the chrome browser')
def launch_browser(context):
    print("In Given")
    # instantiate a chrome options object so you can set the size and headless preference
    context.chrome_options = Options()
    #context.chrome_options.add_argument("--headless")
    #context.chrome_options.add_argument("--window-size=1920x1080")
    #context.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=context.chrome_options)
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://www.d3a.io/")
    assert 'D3A' in context.driver.title
    assert context.driver.current_url == "https://www.d3a.io/" and 'D3A' in context.driver.title


@given(u'Login button is displayed')
def login_button_isdisplayed(context):
    login_button = context.driver.find_element_by_xpath("//header/div[1]/a[1]/button[1]").is_displayed()
    assert login_button is True

@when(u'Enter username and password and Click on login button')
def home_page_isdisplayed(context):
    context.driver.find_element_by_xpath("//header/div[1]/a[1]/button[1]").click()
    context.driver.implicitly_wait(5)
    context.driver.find_element_by_id("email").send_keys("visitbodh@gmail.com")
    context.driver.find_element_by_id("password").send_keys("Sgsits@1")
    context.driver.find_element_by_xpath("//body/div[@id='root']/main[1]/div[2]/div[1]/div[1]/div[1]/form[1]/div[3]/button[1]").click()
    home_logo = context.driver.find_element_by_xpath("//h1[contains(text(),'Home')]").is_displayed()
    assert home_logo is True


@then(u'User must successfully logged in to the D3A.io application')
def verify_loggedin_user(context):
    context.driver.find_element_by_xpath("//div[contains(@class,'side-nav-layout__expand-button__container')]//div[2]").click()
    loggedin_user = context.driver.find_element_by_css_selector("div[class='side-nav__account-controls__username'] p")
    assert loggedin_user.text == "visitbodh@gmail.com"


#ste#2
@given(u'Create Project is accessible via a link to the left panel second icon from the top')
def projects_link_isdisplayed(self):
    projects_link = self.driver.find_element_by_xpath("// button[normalize - space() = 'Projects']").is_enabled()
    assert projects_link is True


@when(u'Click on Projects link')
def projects_page_isdisplayed(context):
    context.driver.find_element_by_xpath("// button[normalize - space() = 'Projects']").click()
    projects_title = context.driver.find_element_by_xpath("//h1[normalize-space()='Projects']")
    assert projects_title.text == "Projects"

@when(u'Click on NEW PROJECT button on the top right')
def new_project_window(context):
    context.driver.find_element_by_xpath("//button[@class='button button--accent button-icon']").click()
    new_project_dialog_box = context.driver.find_element_by_xpath("// div[ @ role = 'dialog']").is_displayed()
    new_project_dialog_box_header = context.driver.find_element_by_xpath("//h3[normalize-space()='New Project']")
    assert new_project_dialog_box is True and new_project_dialog_box_header.text == "New Project"

@when(u'Enter Name, Description and Click on ADD button displayed on New Project dialog box')
def create_new_project_dialog_box(context):
    context.driver.find_element_by_id("email").send_keys("visitbodh@gmail.com")


@then(u'Created Project should be successfully listed')
def verify_project_listing(context):
    Projects_link = context.driver.find_element_by_xpath("// button[normalize - space() = 'Projects']").is_displayed()
    assert Projects_link is True


@then(u'User should be able to edit the Created Project')
def verify_edit_project_list(context):
    context.driver.find_element_by_xpath("// button[normalize - space() = 'Projects']").click()



#step3
@given(u'User has created the Project successfully')
def project_creation(context):
    assert True


@when(u'Click on expand project button')
def expand_project(context):
    assert True


@when(u'Click on NEW SIMULATION button for the selected project')
def new_simulation_button(context):
    assert True


@when(u'Provide simulation details such as simulation name, description, project, start date, end date, solar profile, solar market type, no of spot market, tick length, grid fees, market slot real time duration on New Simulation screen')
def new_simulation_screen(context):
    assert True


@when(u'Click on Next button')
def create_new_simulation(context):
    assert True


@when(u'Click on Projects link and expand project')
def view_simulation_list(context):
    assert True


@then(u'Created Simulation should be successfully listed under the selected Project')
def verify_simulation_list(context):
    assert True


@then(u'User should be able to edit the Created Simulation')
def verify_edit_simulation_list(context):
    assert True