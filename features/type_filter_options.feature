Feature: Type Filter functionality

  Scenario Outline: Validate Type filter in Discover options
    Given the user opens the tmdb page
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    Then user validates movie lists in all pages

    Examples:
      | Dropdown_label | Dropdown_value |
      | Type           | Movie          |
      | Type           | TV Shows       |

