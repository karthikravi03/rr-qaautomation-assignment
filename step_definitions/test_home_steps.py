import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from pages.homepage import HomePage
from utils.config_reader import read_config

scenarios('../features/')
config = read_config()



@pytest.fixture
def homepage(browser):
    return HomePage(browser)


@given("the user opens the tmdb page")
def open_tmdb_page(browser):
    browser.get(config['base_url'])


@when(parsers.parse('user select "{dropdown_label}" as "{dropdown_value}"'))
def select_dropdown_genre_value(homepage, dropdown_label, dropdown_value):
    homepage.set_value_for_type_genre(dropdown_label, dropdown_value)


@then('user store rated movie list')
def step_store_star_rating_movies(homepage):
    homepage.capture_rated_list()


@then(parsers.parse('user compares "{first_star_rating}" and "{second_star_rating}" rated movie list'))
def step_compare_star_rating_lists(homepage, first_star_rating, second_star_rating):
    homepage.compare_star_rated_movies(first_star_rating, second_star_rating)


@then(parsers.parse('user validates movie lists year from "{start_year}" to "{end_year}" in the results'))
def validate_movie_years(homepage, start_year, end_year):
    homepage.validate_movie_year_range(start_year, end_year)


@when(parsers.parse('user select start year as "{start_year}" and end year as "{end_year}"'))
def select_year_range(homepage, start_year, end_year):
    homepage.set_start_end_year(start_year, end_year)


@when(parsers.parse('user select "{type_key}" as "{type_value}"'))
def select_dropdown_type_value(homepage, type_key, type_value):
    homepage.set_value_for_type_genre(type_key, type_value)


@then(parsers.parse('user select star rating as "{star_rating}"'))
def select_star_rating(homepage, star_rating):
    homepage.valid_rating(star_rating)


@then("user validates movie lists in all pages")
def user_validates_movie_lists_in_all_pages(homepage):
    homepage.validate_entire_movie_list()


@then(parsers.parse('user validates movie "{genre}" in all pages'))
def validate_movies_in_all_pages(homepage, genre):
    homepage.validate_movie_genre(genre)


@when(parsers.parse('user click on "{categories_type}"'))
def user_click_on_category(homepage, categories_type):
    homepage.click_category_link(categories_type)


@then(parsers.parse('user verify the selected "{categories_type}" are highlighted'))
def verify_category_highlighted(homepage, categories_type):
    homepage.verify_category_link_highlight(categories_type)

@then(parsers.parse('user check next and previous for "{page_num}" pagination'))
def step_check_pagination(homepage, page_num):
    homepage.validate_pagination_nxt_prev(page_num)

@then(parsers.parse('user check previous to next for "{page_num}" pagination'))
def step_impl(homepage, page_num):
    homepage.validate_pagination_descending(page_num)

@when("user get the entire page count")
def get_total_page_count(homepage):
    homepage.get_total_pages()


@then("user check the pagination and movie tile in page")
def check_pagination_and_movies(homepage):
    homepage.validate_pagination_and_movies()
