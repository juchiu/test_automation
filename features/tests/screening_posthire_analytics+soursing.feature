
Feature: Posthire
  # Enter feature description here
  Background:
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button

  Scenario: posthire actions
    When Open posthire from top navbar
    Then Click first applicant to verify page opened

  Scenario: posthire actions
    When Open posthire from top navbar
    When click recurring checks
    When Add rule
    Then Create new rule
    Then Select openings
    Then request document
    Then Select type
    Then Collect every month
    Then click next
    Then Create

  Scenario: Delete created rule
      When Open posthire from top navbar
      When click_rule_to_delete
      When Click delete