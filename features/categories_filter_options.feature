Feature: Categories Filter functionality


  Scenario Outline: Validate results for Movie type & Genre filter in Discover options
    Given the user opens the tmdb page
    When user click on "<categories_type>"
    Then user verify the selected "<categories_type>" are highlighted

    Examples:
      | categories_type |
      | Popular         |
      | Trend           |
      | Newest          |
      | Top rated       |