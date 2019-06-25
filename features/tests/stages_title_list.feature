# Created by margarita at 2019-05-24
Feature: stages_title_list
  # Enter feature description here
  Background:
   Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button





  Scenario: stages_title_list
    When Click applicants in process link
    When Click carousel
#    When click stages {}
#    Then Title is updated to expected_title
#    Then Verify user can select through stages