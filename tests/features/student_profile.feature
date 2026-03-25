Feature: Student Profile Management
  As a parent or student
  I want to create and manage student profiles
  So that I can generate career analysis reports

  Scenario: Create a valid student profile
    Given the application is running
    When I submit a student profile with name "Ravi Sharma" and standard "10th" and board "CBSE" and state "Maharashtra" and year 2026 and percentage_10th 85.5 and stream "Engineering & Technology"
    Then the profile is created successfully
    And the profile has a unique ID
    And the profile has the correct name "Ravi Sharma"

  Scenario: Create a 12th standard student profile with both percentages
    Given the application is running
    When I submit a student profile with name "Priya Das" and standard "12th" and board "ICSE" and state "West Bengal" and year 2026 and percentage_10th 90.0 and percentage_12th 88.5 and stream "Medical & Healthcare"
    Then the profile is created successfully
    And the profile has percentage_12th set to 88.5

  Scenario: List all student profiles
    Given the application is running
    And a student "Test Student" exists
    When I request the student list
    Then the response contains at least 1 student

  Scenario: Retrieve a specific student profile
    Given the application is running
    And a student "Retrievable Student" exists
    When I request that student's profile by ID
    Then the correct student profile is returned
