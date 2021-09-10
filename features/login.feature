Feature: D3A.io

	Scenario: Login to D3A.io application
		Given I launch the chrome browser
		Then Enter username and password
		And Click on login button
		Then User must successfully logged in to the D3A.io application
		And Landing page must be visible
