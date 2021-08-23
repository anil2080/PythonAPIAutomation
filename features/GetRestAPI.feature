# Created by Anil Kumar at 22-08-2021
Feature: GET Method - Python Jbehave
  # Enter feature description here

  @all @get
Scenario: Get API to fetch the data of page

Given A Get Request with some parameters
When I call requests module Get method with Get URL
Then I should be able to see the related data
