Feature: Career Data
  As a user
  I want to browse career streams
  So that I can understand all available options

  Scenario: All 14 streams are available
    When I request the list of streams
    Then I receive exactly 14 streams

  Scenario: Each stream has top 10 colleges
    Given a stream "Engineering & Technology"
    When I request colleges for India
    Then I receive exactly 10 colleges

  Scenario: Each stream has career options
    Given a stream "Medical & Healthcare"
    When I request career options
    Then I receive at least 1 career option

  Scenario: Career tree is navigable
    When I build the career tree
    Then the root node has name "Career Map"
    And the tree has an "After 10th Standard" node with 14 children
