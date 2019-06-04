
  Feature: Login and verify locations presented on opening page
    Background:
       Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

  Scenario: Every location on the page has 'applicants' text

    Then Every location on the page has 'applicants in process' text
    And Every location on the page has actions

