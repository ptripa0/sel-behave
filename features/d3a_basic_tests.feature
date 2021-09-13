Feature: Test basic operations of d3a.io


  Scenario Outline: Validate that a user with invalid credentials is unable to Login to D3A.io application
    Given User navigates to login page of D3A.io application
    When Enter username "<username>" and password "<password>" and Click on login button
    Then User with invalid credentials, username "<username>" and password "<password>" should not be allowed to login to the D3A.io
    Examples:
      | username             | password  |
      | randomuser@gmail.com | Sgsits@1  |
      | randomuser@gmail.com | Invalid@1 |


  Scenario Outline: Validate that a valid user is able to Login to D3A.io application
    Given User navigates to login page of D3A.io application
    When Enter username "<username>" and password "<password>" and Click on login button
    Then User "<username>" with valid credentials should be successfully logged in to the D3A.io application
    Examples:
      | username            | password |
      | visitbodh@gmail.com | Sgsits@1 |


  Scenario Outline: Validate that a logged in user is able to create a project
    Given Create Project is accessible via a link to the left panel second icon from the top
    When Click on Projects link
    And Click on NEW PROJECT button on the top right
    And Enter Name "<project_name>", Description "<project_description>" and Click on ADD button displayed on New Project dialog box
    Then Created Project with Name "<project_name>" and Description "<project_description>" should be successfully listed
    And User should be able to edit the Created Project "<project_name>"
    Examples:
      | project_name              | project_description                 |
      | Project_for qa!123 /'"",. | Project_for qa.description@12~ /';" |

  Scenario Outline: Validate that a logged in user can create a simulation
    Given User has created the Project "<project_name>" successfully
    When Click on expand project button
    And Click on NEW SIMULATION button for the selected project
    And Provide simulation details such as simulation name "<simulation_name>", description "<sim_description>", project "<project_name>", no of spot market "<market_count>", tick length "<tick_length>", market slot real time duration "<slot_length>" on New Simulation screen
    And Click on Projects link and expand project
    Then Created Simulation should be successfully listed for the selected Project "<project_name>", Simulation "<simulation_name>", "<sim_description>" and market count "<market_count>"
    And Created Simulation should also be successfully listed under the selected Project "<project_name>" by searching the project
    Examples:
      | project_name              | simulation_name      | sim_description | market_count | tick_length | slot_length |
      | Project_for qa!123 /'"",. | default simulationqa | qa description  | 3            | 90          | 900         |
