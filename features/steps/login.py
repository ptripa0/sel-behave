from behave import *


@given(u'I launch the chrome browser')
def step_impl(context):
    print("In Given")
    assert True


@then(u'Enter username and password')
def step_impl(context):
    assert context.failed is False


@then(u'Click on login button')
def step_impl(context):
    assert context.failed is False


@then(u'User must successfully logged in to the D3A.io application')
def step_impl(context):
    assert context.failed is False


@then(u'Landing page must be visible')
def step_impl(context):
    assert context.failed is False
