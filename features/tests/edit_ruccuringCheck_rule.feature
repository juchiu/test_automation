# Created by margarita at 2019-06-14
Feature: #Enter feature name here
  # Enter feature description here
   Background:
      Given   Open login page
      When    Input usernameStr
      Then    Input passwordStr
      When    Click LOG IN button

  Scenario: Edit recurring check rule
      When Open posthire from top navbar2
      When Click recurring checks2
      When click rule to edit
      Then edit reminder