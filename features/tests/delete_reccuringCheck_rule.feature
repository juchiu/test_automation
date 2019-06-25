# Created by margarita at 2019-06-14
Feature: Delete created rule
  # Enter feature description here

    Background:
      Given   Open login page
      When    Input usernameStr
      Then    Input passwordStr
      When    Click LOG IN button

  Scenario: Delete created rule
      When Open posthire from top navbar1
      When Click recurring checks1
      When click_rule_to_delete
      When Click delete