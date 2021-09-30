D3A.io is a web based application, for which automated test suite is created with testcases in Gherkin syntax (given/when/then).

Given solution used follwing technology stack:
Selenium, Python, BDD (behave), PyCharm, GitHub, GitHub actions for CI, Behave/Allure test reports, Windows/Mac/Linux

Test execution command:
behave -f behave_html_formatter:HTMLFormatter -o reports/behave-test-report.html features






Below is the information of planned features and tests:
\n
Feature: Test basic operations of d3a.io
\n
  Scenario Outline: Validate that a user with invalid credentials is unable to Login to D3A.io application\n
  Scenario Outline: Validate that a valid user is able to Login to D3A.io application\n
  Scenario Outline: Validate that a logged in user is able to create a project\n
  Scenario Outline: Validate that a logged in user can create a simulation\n
 




