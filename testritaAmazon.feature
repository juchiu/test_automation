


# Created by margarita at 2019-05-04
Feature: Test Amazon HIGH
  # Enter feature description here

  Scenario: # User can search product on Amazon
    # Enter steps here
    Given open Amazon page
    When input shoes into amazon search field
    And click on amazon search icon
    Then Amazon product results for shoes are shown
