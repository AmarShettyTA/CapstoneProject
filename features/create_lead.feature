Feature: Salesforce create lead account and convert the lead

  Scenario Outline: Create Lead account
    Given User logs in to salesforce
    When User enters "<username>" and "<password>"
    Then User clicks on login
    Then User is on dashboard page
    Then User is on Home Page
    Then User clicks on Accounts dropdown and new account
    Then User enters "<account name>"
    Then User clicks on Save account button
    Then Verify Account is Created by the "<account name>"
    When User clicks on Lead dropdown and clicks New Lead
    Then User enters "<last name>" and "<company>"
    Then Click on Save button
    Then Verify Lead is Created using "<last name>"
    When User clicks on convert
    Then User choses account type: "<account type>" and account name: "<account name>"
    Then User clicks on Convert button
    Then Close Lead Popup screen

    Examples:
      | username                   | password    | account name | last name | company | account type  |
      | amar.shetty-1wru@force.com | Grim@123    | Hogwarts     | Dumble    | Dore    | Existing      |

