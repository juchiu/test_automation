# Created by margarita at 2019-06-24
Feature: Search applicants in the dashboard

   Background:
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button

  Scenario: search by phone#
    When Click applicants in process
    When first search by phone number

    Scenario: Search1 by email
    When Click applicants in process
    When Search1 by email

    Scenario: Search2 text
    When Click applicants in process
    When Search2 text

