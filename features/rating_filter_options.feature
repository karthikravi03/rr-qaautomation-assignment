Feature: Rating Filter functionality

  Scenario Outline: Validate Rating filter in Discover options
    Given the user opens the tmdb page
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    Then user select star rating as "<Star_Rating>"

    Examples:
      | Dropdown_label | Dropdown_value | Star_Rating |
      | Type           | Movie          | 0           |
      | Type           | Movie          | 1.3         |
      | Type           | TV Shows       | 3.5         |
      | Type           | TV Shows       | 5.5         |

  Scenario Outline: Validate Rating filter in Discover options
    Given the user opens the tmdb page
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    Then user compares "<first_Star_Rating>" and "<second_Star_Rating>" rated movie list

    Examples:
      | Dropdown_label | Dropdown_value | first_Star_Rating | second_Star_Rating |
      | Type           | Movie          | 1.0               | 2.0                |
      | Type           | Movie          | 1.0               | 5.0                |
      | Type           | TV Shows       | 1.0               | 4.0                |
      | Type           | TV Shows       | 2.0               | 5.0                |