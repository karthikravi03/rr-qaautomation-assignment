Feature: Genre Filter functionality

  Scenario Outline: Validate results for Movie type & Genre filter in Discover options
    Given the user opens the tmdb page
    When user select "<Type_key>" as "<Type_value>"
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    Then user validates movie "<Genre>" in all pages

    Examples:
      | Dropdown_label | Dropdown_value | Genre     | Type_key | Type_value |
      | Genre          | Action         | Action    | Type     | Movie      |
      | Genre          | Adventure      | Adventure | Type     | Movie      |
      | Genre          | Animation      | Animation | Type     | Movie      |
      | Genre          | Comedy         | Comedy    | Type     | Movie      |
      | Genre          | Music          | Music     | Type     | Movie      |
      | Genre          | Romance        | Romance   | Type     | Movie      |

  Scenario Outline: Validate results for TV Shows type & Genre filter in Discover options
    Given the user opens the tmdb page
    When user select "<Type_key>" as "<Type_value>"
    When user select "<Dropdown_label>" as "<Dropdown_value>"
    Then user validates movie "<Genre>" in all pages

    Examples:
      | Dropdown_label | Dropdown_value     | Genre              | Type_key | Type_value |
      | Genre          | Action & Adventure | Action & Adventure | Type     | TV Shows   |
      | Genre          | News               | News               | Type     | TV Shows   |
      | Genre          | Comedy             | Comedy             | Type     | TV Shows   |
      | Genre          | Talk               | Talk               | Type     | TV Shows   |
      | Genre          | Soap               | Soap               | Type     | TV Shows   |

