# Created by margarita at 2019-05-23
Feature: Opening's dashboard
  # Enter feature description here
Background:
   Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

  Scenario: Opening's dashboard
    Then Click actions dropdown
    Then options
   Then click_actions