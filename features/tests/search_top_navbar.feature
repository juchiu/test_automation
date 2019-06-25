# Created by margarita at 2019-06-10
Feature: Search top navbar

  Background:
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button



  Scenario: search by phone#
  When search by phone#
    When assert


  Scenario: Search by email
    When By email
    When assert to verify search by email success


  Scenario: Search text
    Then Search by text
    When assert to verify search by text success
    Then Open first opening/stage from search results page
    Then verify applicant details opened