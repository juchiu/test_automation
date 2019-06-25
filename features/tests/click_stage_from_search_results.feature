Feature: Click funnel to open stage and opening

  Background:
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button

 Scenario: test
    When search for applicant by phone number
    Then Open first opening/stage
    Then verify page opened
