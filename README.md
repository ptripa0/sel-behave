Google docs link: https://docs.google.com/document/d/1tvvROg6gFdr_UnavcBNQPUw9X8S_F9W9nZSdUEBtt3Q/edit?usp=sharing

This breif Test Plan describes about the application under test, test approach, test results and observations.

D3A.io is a web based application, for which automated test suite needed to be created either using Cypress or Selenium (in Javascript or Python).
Preferably writing the testcases in Gherkin syntax (given/when/then).

Given solution used follwing technology stack:
Selenium, Python, BDD (behave), PyCharm, GitHub, GitHub actions for CI, Behave/Allure test reports, Windows/Mac/Linux

Test execution command:
behave -f behave_html_formatter:HTMLFormatter -o reports/behave-test-report.html features






Below is the information of planned features and tests:

Feature: Test basic operations of d3a.io

  Scenario Outline: Validate that a user with invalid credentials is unable to Login to D3A.io application
  Scenario Outline: Validate that a valid user is able to Login to D3A.io application
  Scenario Outline: Validate that a logged in user is able to create a project
  Scenario Outline: Validate that a logged in user can create a simulation
 




Following are the bugs\observations, encountered while executing automation tests.

1. No simulations are shown for the projects when user uses search option to display Project listing.
However, if user go directly to the project by browsing, then simulations are displayed as expected.

2. Simulation name textbox accepts length of 27 characters only.

Description - User is clueless about the restriction and programmatically it gets truncated.

3. If Tick LengthSeconds = -1 is given while creating a simulation, application shows inappropriate message.

Actual message-
Invalid tick_length (86399 sec, limits: [1 sec, 90 sec])

Acceptaed message-
Invalid tick_length (-1 sec, limits: [1 sec, 90 sec])


4. If Tick length is given as below, application displays that error message was undefined.  
tickLengthSeconds: -212345678901234567890

Actual result -
Error message was undefined

Expected result - Error message should be informative such as..
{"errors":[{"message":"Int cannot represent non 32-bit signed integer value: -212345678901234570000"}]}

or
Invalid tick_length (-212345678901234567890 sec, limits: [1 sec, 90 sec])


5. If the value of "Number of spot markets" is given as below, application displays that error message was undefined.
Number of spot markets = 2147483649

Actual result -
Error message was undefined

Expected result - Error message should be informative such as..
{"errors":[{"message":"Int cannot represent non 32-bit signed integer value: 12345678901234567000"}]}

or

Number of spot markets must be a number between 0 and 2147483647

6. If the value of "Market slot real time duration" is given as below, application does not throw errors and displays that error message was undefined.
Market slot real time duration = -2e

Actual result -
Error message was undefined

Expected result-
Market slot real time duration must be a number between 0 and 900


7. Application flow observation: Create simulation flow can be enhanced to make more user friendly. 
After creating a simulation, user must complete the modellings after the settings. This flow is less intuitive.
There is no confirmation message that simulation is created. Furthermore Modelling screen, no display of name of project and simulation.

Once user clicks on New Simulation button and New Simulation form is displayed, there is no option to cancel it if user wants to.

I found overall user experience as high for the given application.


Thanks
