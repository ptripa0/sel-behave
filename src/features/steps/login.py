from behave import *


@given(u'I launch the chrome browser')
def step_impl(context):
    print("In Given")
    raise NotImplementedError(u'STEP: Given I launch the chrome browser')


@then(u'Enter username and password')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Enter username and password')


@then(u'Click on login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Click on login button')


@then(u'User must successfully logged in to the D3A.io application')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User must successfully logged in to the D3A.io application')


@then(u'Landing page must be visible')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Landing page must be visible')
