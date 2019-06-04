# Created by margarita at 2019-05-21
Feature: Navigational bar loop
  # Enter feature description here
Background:
  Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button


  Scenario: Click through navigational bar elements
    Then Every element clickable
    Then Click first 3