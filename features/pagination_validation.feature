Feature: Pagination functionality


  Scenario: Validate movies are present in each page
    Given the user opens the tmdb page
    When user get the entire page count
    Then user check the pagination and movie tile in page


  Scenario Outline: Validate pagination from ascending to descending
    Given the user opens the tmdb page
    When user get the entire page count
    Then user check next and previous for "<page_num>" pagination
    Examples:
      | page_num |
      | 10       |


  Scenario Outline: Validate pagination from descending to ascending
    Given the user opens the tmdb page
    When user get the entire page count
    Then user check previous to next for "<page_num>" pagination
    Examples:
      | page_num |
      | 10       |
