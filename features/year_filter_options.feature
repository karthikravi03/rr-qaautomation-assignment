Feature: Year Filter functionality

  Scenario Outline: Validate Year filter in Discover options
    Given the user opens the tmdb page
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    When user select start year as "<start_year>" and end year as "<end_year>"
    Then user validates movie lists year from "<start_year>" to "<end_year>" in the results

    Examples:
      | Dropdown_label | Dropdown_value |start_year| end_year|
      | Type           | Movie          | 2000     |2010     |
      | Type           | TV Shows       | 2000     |2010     |