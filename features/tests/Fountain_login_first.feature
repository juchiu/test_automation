# Created by margarita at 2019-05-05
Feature:  login page, multiple tests


  Scenario: Login
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button
