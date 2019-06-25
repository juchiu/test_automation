# Created by margarita at 2019-06-24
Feature: Jobs directory
  # Enter feature description here

  Scenario: Search openings in jobs directory
  Given Open Jobs directory
  When select_country
  When select_US
  Then Select company
  Then select_Fountain
  Then And search openings in jobs directory