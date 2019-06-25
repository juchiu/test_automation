# Created by margarita at 2019-06-04
Feature: Select multiple applicants and check bulk edit functionality
  # Enter feature description here

     Background:
       Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

     Scenario: Bulk actions with 2+ applicants
     When Click applicants in process link2
     Then Select two users
     Then Click Bulk Actions dropdown and verify actions