
Feature: Check nav bar dropdown
  # Enter feature description here
   Background:
   Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

   Scenario: check nav bar dropdown
        When select first dropdown