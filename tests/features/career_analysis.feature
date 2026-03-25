Feature: Career Analysis Engine
  As a parent/student
  I want to generate a career analysis
  So I can understand which career stream suits the student

  Scenario: Deterministic analysis produces consistent results
    Given a student profile with name "Consistent Student" and 10th percentage 80.0 and stream "Engineering & Technology"
    When I run the analysis twice
    Then both results are identical

  Scenario: Analysis includes suitability score
    Given a student profile with name "Scored Student" and 10th percentage 85.0 and stream "Medical & Healthcare"
    When I run the analysis
    Then the result has a suitability score between 0 and 100

  Scenario: Analysis includes career options
    Given a student profile with name "Career Student" and 10th percentage 75.0 and stream "Commerce, Finance & Business"
    When I run the analysis
    Then the result includes at least 1 career option
    And the result includes at least 1 industry

  Scenario: Analysis includes top colleges
    Given a student profile with name "College Student" and 10th percentage 90.0 and stream "Engineering & Technology" and state "Maharashtra"
    When I run the analysis
    Then the result includes at least 5 top colleges

  Scenario: Analysis flags insufficient data
    Given a student profile with name "Insufficient Student" and 12th standard and no 12th percentage
    When I run the analysis
    Then the result flags data insufficiency

  Scenario: Analysis includes top 2 recommendations
    Given a student profile with name "Recommended Student" and 10th percentage 82.0 and stream "Science & Research"
    When I run the analysis
    Then the result includes exactly 2 top recommendations
