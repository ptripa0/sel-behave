Feature: Test basic operations of d3a.io

	Scenario: Login to D3A.io application
		Given User launches the chrome browser
		And Login button is displayed
		When Enter username and password and Click on login button
		Then User must successfully logged in to the D3A.io application

	Scenario: Validate that a logged in user is able to create a project
		Given Create Project is accessible via a link to the left panel second icon from the top
		When Click on Projects link
		And Click on NEW PROJECT button on the top right
		And Enter Name, Description and Click on ADD button displayed on New Project dialog box
		Then Created Project should be successfully listed
		And User should be able to edit the Created Project

	Scenario: Validate that a logged in user can create a simulation
		Given User has created the Project successfully
		When Click on expand project button
		And Click on NEW SIMULATION button for the selected project
		And Provide simulation details such as simulation name, description, project, start date, end date, solar profile, solar market type, no of spot market, tick length, grid fees, market slot real time duration on New Simulation screen
		And Click on Next button
		And Click on Projects link and expand project
		Then Created Simulation should be successfully listed under the selected Project
		And User should be able to edit the Created Simulation