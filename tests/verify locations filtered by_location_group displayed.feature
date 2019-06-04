# Created by margarita at 2019-05-22
Feature: verify locations filtered by_location_group
  # Log in
  # filter by_location_group
  # verify locations displayed
Background:
   Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

  Scenario: verify locations filtered by_location_group
    Then Click dropdown to see filtering options
    Then select by location group
#    Then Verify filtered by_location_group