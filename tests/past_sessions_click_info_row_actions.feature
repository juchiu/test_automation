# Created by margarita at 2019-05-30
Feature: Sessions flow nav bar

   Background:
       Given   Open login page
       When    Input usernameStr
       Then    Input passwordStr
       When    Click LOG IN button

    Scenario: Sessions
      When Click Sessions
      When Click past
      When Verify past sessions
      Then Click info row actions
      Then Close manage applicants modal
      Then Click info row actions and close
      Then Export
