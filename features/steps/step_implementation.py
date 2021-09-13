from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os
from utilities.locator_resources import *


#  Scenario - 1 steps
@given('User navigates to login page of D3A.io application')
def user_navigates_to_login_page_of_application(context):
    try:
        if context.is_logged_in is True:
            context.driver.find_element_by_xpath(locator_resources.settings_button_xpath).click()
            context.driver.implicitly_wait(1)
            context.driver.find_element_by_css_selector(locator_resources.logout_button_css).click()
            context.is_logged_in = False
            assert 'D3A' in context.driver.title

    except:
        context.driver.refresh()
        context.driver.implicitly_wait(1)
        if context.driver.find_element_by_xpath(locator_resources.signup_button_xpath).is_displayed() is True:
            context.driver.find_element_by_xpath(locator_resources.signup_button_xpath).click()

        context.driver.implicitly_wait(1)
        context.driver.find_element_by_id("email").send_keys(get_config()['User']['username'])
        context.driver.find_element_by_id("password").send_keys(get_config()['User']['password'])
        context.driver.find_element_by_xpath(locator_resources.login_button_xpath).click()
        context.is_logged_in = True
        assert 'D3A' in context.driver.title


@when('Enter username "{username}" and password "{password}" and Click on login button')
def home_page_isdisplayed(context, username, password):
    if context.is_logged_in is False:
        context.driver.implicitly_wait(5)
        context.driver.find_element_by_id("email").send_keys(username)
        context.driver.find_element_by_id("password").send_keys(password)
        try:

            context.driver.find_element_by_css_selector(".button.button--accent").click()
            context.driver.implicitly_wait(1)
            home_logo = context.driver.find_element_by_xpath(locator_resources.home_logo_xpath).is_displayed()
            context.is_logged_in is True
            assert home_logo is True

        except:

            error_msg = context.driver.find_element_by_xpath(locator_resources.invalid_login_error_xpath)

            if error_msg.is_displayed() is True:
                assert error_msg.text == 'Please, enter valid credentials' or 'User has tried to log in too many times (more than 4) and is currently locked out.'
            else:
                assert False, "Login test failed"

    elif context.is_logged_in is True:
        Projects_link = context.driver.find_element_by_xpath(locator_resources.projects_link_xpath).is_displayed()
        assert Projects_link is True


@then(
    'User with invalid credentials, username "{username}" and password "{password}" should not be allowed to login to the D3A.io')
def verify_invalid_user_credentials(context, username, password):
    if context.driver.current_url != "https://www.d3a.io/" and context.is_logged_in is False:
        try:
            context.driver.find_element_by_xpath(locator_resources.side_nav_layout_button_xpath).click()
        except:
            assert True, "Invalid User"


@then('User "{username}" with valid credentials should be successfully logged in to the D3A.io application')
def verify_loggedin_user(context, username):
    context.driver.find_element_by_xpath(locator_resources.side_nav_layout_button_xpath).click()
    loggedin_user = context.driver.find_element_by_css_selector(locator_resources.logged_in_user_css)
    context.is_logged_in is True
    assert loggedin_user.text == username


# Scenario - 2 steps
@given('Create Project is accessible via a link to the left panel second icon from the top')
def projects_link_isdisplayed(context):
    if context.is_logged_in is True:
        context.driver.find_element_by_xpath(locator_resources.side_nav_layout_button_xpath).click()
        projects_link = context.driver.find_element_by_css_selector(locator_resources.logged_in_user_css).is_displayed()
        assert projects_link is True


@when('Click on Projects link')
def projects_page_isdisplayed(context):
    if context.is_logged_in is True:
        context.driver.find_element_by_xpath(locator_resources.projects_link_xpath).click()
        projects_title = context.driver.find_element_by_xpath(locator_resources.projects_title_xpath)
        assert projects_title.text == "Projects"


@when('Click on NEW PROJECT button on the top right')
def new_project_window(context):
    if context.is_logged_in is True:
        context.driver.find_element_by_xpath(locator_resources.new_project_button_xpath).click()
        new_project_dialog_box = context.driver.find_element_by_css_selector(
            locator_resources.new_project_dialog_box_xpath).is_displayed()
        new_project_dialog_box_header = context.driver.find_element_by_xpath(
            locator_resources.new_project_dialog_box_header_xpath)
        assert new_project_dialog_box is True and new_project_dialog_box_header.text == "New Project"


@when(
    'Enter Name "{project_name}", Description "{project_description}" and Click on ADD button displayed on New Project dialog box')
def create_new_project_dialog_box(context, project_name, project_description):
    if context.is_logged_in is True:
        context.driver.find_element_by_id(locator_resources.new_project_field_xpath).send_keys(project_name)
        context.driver.find_element_by_id(locator_resources.project_name_textarea_xpath).send_keys(project_description)
        context.driver.find_element_by_css_selector(locator_resources.project_button_css).click()
        context.driver.find_elements_by_css_selector(locator_resources.save_project_list_css)
        projects_link = context.driver.find_element_by_xpath(locator_resources.project_header_xpath).is_displayed()
        assert projects_link is True


@then(
    'Created Project with Name "{project_name}" and Description "{project_description}" should be successfully listed')
def verify_project_listing(context, project_name, project_description):
    if context.is_logged_in is True:
        try:
            context.driver.find_element_by_css_selector(
                locator_resources.project_list_placeholder_search_css).send_keys(project_name)
            context.driver.find_element_by_css_selector(locator_resources.saved_projects_list_css).is_displayed()
            assert context.driver.find_element_by_css_selector(
                locator_resources.saved_projects_headline_css).text == project_name
            assert context.driver.find_element_by_css_selector(locator_resources.saved_projects_cog_css).is_displayed()
            assert context.driver.find_element_by_css_selector(
                locator_resources.project_description_css).text == project_description
            context.driver.find_element_by_css_selector(locator_resources.saved_projects_headline_name_css).click()
            assert context.driver.find_element_by_css_selector(
                locator_resources.saved_projects_empty_list_css).text == "No simulations to show for this project"
        except:
            assert False, "Project listing test failed"


@then('User should be able to edit the Created Project "{project_name}"')
def verify_edit_project_list(context, project_name):
    if context.is_logged_in is True:
        context.driver.find_element_by_css_selector(locator_resources.edit_projects_list_css).send_keys(project_name)
        context.driver.find_element_by_xpath(locator_resources.edit_projects_icon_xpath).click()
        rename_project = context.driver.find_element_by_xpath(locator_resources.rename_projects_button_xpath).text
        delete_project = context.driver.find_element_by_xpath(locator_resources.delete_projects_button_xpath).text
        assert rename_project == 'Rename' and delete_project == 'Delete'


# Scenario - 3 steps
@given('User has created the Project "{project_name}" successfully')
def project_creation(context, project_name):
    context.driver.find_element_by_xpath(locator_resources.side_nav_layout_button_xpath).click()
    context.driver.find_element_by_xpath(locator_resources.projects_link_xpath).click()
    context.driver.find_element_by_css_selector(locator_resources.projects_search_css).send_keys(project_name)
    assert context.driver.find_element_by_css_selector(locator_resources.saved_projects_list_css).is_displayed()
    assert context.driver.find_element_by_css_selector(
        locator_resources.saved_projects_headline_css).text == project_name


@when('Click on expand project button')
def expand_project(context):
    try:
        context.driver.find_element_by_css_selector(locator_resources.save_project_button_css).click()
        assert True
    except:
        assert False


@when('Click on NEW SIMULATION button for the selected project')
def new_simulation_button(context):
    context.driver.find_element_by_xpath(locator_resources.new_simulation_button_xpath).click()
    simulation_settings_form = context.driver.find_element_by_xpath(
        locator_resources.simulation_settings_form_xpath).is_displayed()
    assert simulation_settings_form is True


@when(
    'Provide simulation details such as simulation name "{simulation_name}", description "{sim_description}", project "{project_name}", no of spot market "{market_count}", tick length "{tick_length}", market slot real time duration "{slot_length}" on New Simulation screen')
def new_simulation_screen(context, simulation_name, sim_description, project_name, market_count, tick_length,
                          slot_length):
    context.driver.implicitly_wait(2)
    context.driver.find_element_by_css_selector(locator_resources.simulation_name_css).send_keys('qa')
    context.driver.find_element_by_css_selector(locator_resources.simulation_description_css).clear()
    context.driver.find_element_by_css_selector(locator_resources.simulation_description_css).send_keys(sim_description)
    context.driver.find_element_by_css_selector(locator_resources.simulation_market_count_css).clear()
    context.driver.find_element_by_css_selector(locator_resources.simulation_market_count_css).send_keys(market_count)
    context.driver.find_element_by_css_selector(locator_resources.simulation_tickLengthSeconds_css).clear()
    context.driver.find_element_by_css_selector(locator_resources.simulation_tickLengthSeconds_css).send_keys(
        tick_length)
    context.driver.find_element_by_css_selector(locator_resources.simulation_slotLengthRealtimeSeconds_css).clear()
    context.driver.find_element_by_css_selector(locator_resources.simulation_slotLengthRealtimeSeconds_css).send_keys(
        slot_length)
    assert context.driver.find_element_by_xpath(locator_resources.new_simulation_text_xpath).text == 'New Simulation'
    context.driver.find_element_by_css_selector(locator_resources.submit_new_simulation_xpath).click()
    assert context.driver.find_element_by_xpath(locator_resources.new_modelling_header_text_xpath).text == 'Modelling'


@when('Click on Projects link and expand project')
def view_simulation_list(context):
    context.driver.find_element_by_xpath(locator_resources.side_nav_layout_button_xpath).click()
    context.driver.find_element_by_xpath(locator_resources.projects_link_xpath).click()
    projects_link = context.driver.find_element_by_xpath(locator_resources.projects_link_xpath).is_displayed()
    assert projects_link is True
    assert context.driver.find_element_by_css_selector(locator_resources.save_project_list_css) is not None


@then(
    'Created Simulation should be successfully listed for the selected Project "{project_name}", Simulation "{simulation_name}", "{sim_description}" and market count "{market_count}"')
def verify_simulation_list_displayed_on_projects_page(context, project_name, simulation_name, sim_description,
                                                      market_count):
    # Verifying simulation listing components
    if simulation_name in context.driver.find_element_by_css_selector(
            locator_resources.simulation_listing_main_content_css).text:
        assert True

    if sim_description in context.driver.find_element_by_css_selector(
            locator_resources.simulation_listing_main_content_css).text:
        assert True

    # Verifying CSS values are similar for settings and modelling icons
    settings_icon_css_value = context.driver.find_element_by_xpath(
        locator_resources.settings_icon_css).value_of_css_property('color')
    modelling_icon_css_value = context.driver.find_element_by_xpath(
        locator_resources.modelling_icon_css).value_of_css_property('color')
    assert settings_icon_css_value == modelling_icon_css_value

    assert context.driver.find_element_by_css_selector(locator_resources.simulation_listing_date_css).text is not None
    assert context.driver.find_element_by_xpath(locator_resources.button_icon_icon_settings_dots_xpath).is_enabled()
    assert context.driver.find_element_by_xpath(locator_resources.button_icon_icon_modelling_dots_xpath).is_enabled()
    assert context.driver.find_element_by_xpath(locator_resources.button_new_modelling_list_xpath).is_displayed()
    assert context.driver.find_element_by_xpath(
        locator_resources.setting_button_new_modelling_list_xpath).is_displayed()


@then(
    'Created Simulation should also be successfully listed under the selected Project "{project_name}" by searching the project')
def verify_simulation_list_by_search(context, project_name):
    context.driver.find_element_by_css_selector(locator_resources.project_list_placeholder_search_css).send_keys(
        project_name)
    assert context.driver.find_element_by_css_selector(locator_resources.saved_projects_list_css).is_displayed()
    assert context.driver.find_element_by_xpath(
        locator_resources.simulation_listing_content_by_search_xpath).text is not None

    if context.driver.find_element_by_css_selector(
            locator_resources.saved_projects_empty_list_css).text == 'No simulations to show for this project':
        context.driver.find_element_by_xpath(locator_resources.search_project_by_xpath).send_keys(project_name)
        context.driver.find_element_by_xpath(locator_resources.setting_button_by_xpath).click()
        context.driver.find_element_by_xpath(locator_resources.delete_button_by_xpath).click()
        context.driver.find_element_by_xpath(locator_resources.confirm_delete_button_by_xpath).click()
        context.driver.implicitly_wait(2)

        assert False, 'No simulations to show for this project'
