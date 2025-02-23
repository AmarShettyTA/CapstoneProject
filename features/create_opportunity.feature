Feature: Salesforce create opportunity and attach to account

  Scenario Outline: Create opportunity and attach to account
    Given User logs in to salesforce
    When User enters "<username>" and "<password>"
    And User clicks on login
    Then User is on dashboard page
    Then User is on Home Page
    Then User clicks on Accounts dropdown and new account
    Then User enters "<account name>"
    Then User clicks on Save button
    Then Verify Account is Created by the "<account name>"
    Then User clicks on contact dropdown and clicks new contact
    Then User enters "<last name>" and selects the "<account name>"
    Then User clicks on save contact button
    Then Verify contact is created by the "<last name>"
    Then User clicks on opportunity dropdown and clicks new opportunity
    Then User enters "<opportunity name>" and Select the "<account name>"
    Then User enters opportunity close date: "<close date>"
    Then User selects opportunity stage: "<opportunity stage>"
    Then User selects opportunity forecast: "<opportunity forecast>"
    Then User clicks on save button contact button
    Then Verify opportunity is created by the "<opportunity name>"


    Examples:
      | username                   | password    | account name | last name | opportunity name | close date | opportunity stage | opportunity forecast |
      | amar.shetty-1wru@force.com | Grim@123    | FarCry       | Vyas      | Brody            | 25/03/2025 | Propose           | Commit               |

