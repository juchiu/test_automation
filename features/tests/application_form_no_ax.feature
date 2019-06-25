
Feature: Check application form with AX

  Scenario: Complete and submit application form without AX enabled
    Given Open application form
    When Fill out application form
    Then Click submit
    Then page opened