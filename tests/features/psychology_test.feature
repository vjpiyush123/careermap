Feature: Psychology Aptitude Test
  As a student
  I want to take a psychology test
  So that my career analysis considers my aptitudes

  Scenario: Retrieve psychology test questions
    Given the application is running
    When I request the psychology test
    Then I receive 20 questions
    And each question has 4 options

  Scenario: Submit psychology test answers
    Given the application is running
    And a student "Psych Student" exists
    When I submit answers for all 20 questions
    Then I receive aptitude scores for all 14 streams
    And the student profile is updated with psychology scores

  Scenario: Psychology scores are normalised 0-100
    Given the application is running
    And a student "Score Student" exists
    When I submit answers for all 20 questions
    Then all scores are between 0 and 100
