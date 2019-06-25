# Created by margarita at 2019-06-24
  Feature: Applicant details

   Background:
    Given   Open login page
    When    Input usernameStr
    Then    Input passwordStr
    When    Click LOG IN button


  Scenario: Applicant details
    When Click a in process link
    When click first applicant
    Then Click history
    Then click Files

  Scenario: applicant details send email now
    When Click a in process link
    When click first applicant
    When Click actions
    Then click send email
    Then Send email now

  Scenario: applicant details send email later
    When Click a in process link
    When click first applicant
    When Click actions
    Then click send email
    Then click send email later

  Scenario: applicant details send Text/SMS now
    When Click a in process link
    When click first applicant
    When Click actions
    Then Click Send Text/SMS now

  Scenario: applicant details send Text/SMS later
    When Click a in process link
    When click first applicant
    When Click actions
    Then Click Send Text/SMS later

  Scenario: Unsibscribe from SMS and reactivate SMS
    When Click a in process link
    When click first applicant
    When Click actions
    Then Unsibscribe from SMS and reactivate SMS

  Scenario: Unsubscribe from Email and Reactivate Email
    When Click a in process link
    When click first applicant
    When Click actions
    Then Unsubscribe from Email and reactivate Email

  Scenario: Edit applicant
    When Click a in process link
    When click first applicant
    When Click actions
    Then Option to edit applicant