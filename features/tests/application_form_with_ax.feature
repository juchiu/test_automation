
Feature: Check application form with AX

  Scenario: Complete and submit application form with AX enabled
    Given Open AX application form
    When Fill out AX application form
    Then Click submit button
    Then Landing page opened