# Created by Anil Kumar at 23-08-2021
Feature: POST Method - REQUESTS MODULE

  @post @all
Scenario Outline: Post API to create a user in database

Given A post Request with some parameters
When I call Requests post method with request payload to create user "<user>"
Then I should be able to create a user successfully "<user>"

    Examples:
    |user|
    |ABCD|
    |XYZD|
    |LMNO|