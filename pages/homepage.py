import time
from _pydecimal import Decimal
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import get_logger



class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.popular_link = (By.XPATH, "//a[text()='Popular']")
        self.trend_link = (By.XPATH, "//a[text()='Trend']")
        self.newest_link = (By.XPATH, "//a[text()='Newest']")
        self.top_rated_link = (By.XPATH, "//a[text()='Top rated']")
        self.type_dropdown = (By.XPATH, "//p[text()='Type']//following::div[1]")
        self.genre_dropdown = (By.XPATH, "//p[text()='Genre']//following::div[1]")
        self.start_year_dropdown = (By.XPATH, "//p[text()='Year']//following::div[2]")
        self.end_year_dropdown = (By.XPATH, "//span[@class='text-white mx-2']/following-sibling::div")
        self.last_page_num = (By.XPATH, "//div[@id='react-paginate']//li[position()=last()-1]/a")
        self.next_page = (By.XPATH, "//div[@id='react-paginate']//li[position()=last()]/a")
        self.prev_page = (By.XPATH, "//div[@id='react-paginate']//li[@class='previous']")
        self.highlight_text = (By.XPATH, "//ul[@class='list-none flex']/li")
        self.highlight_text_value = (By.XPATH, "//ul[@class='list-none flex']/li[contains(@class,'text-white')]/a")
        self.wait_spin=(By.XPATH, "//div[@class='w-full h-full overflow-scroll']")
        self.movie_tile=(By.XPATH, "//div[@class='flex flex-col items-center']")

    def click_popular(self):
        self.wait_and_click(self.popular_link)

    def click_trend(self):
        self.wait_and_click(self.trend_link)

    def click_newest(self):
        self.wait_and_click(self.newest_link)

    def click_top_rated(self):
        self.wait_and_click(self.top_rated_link)

    def click_select_type_dropdown(self, type_value):
        """
        Selects a movie type from the 'Type' dropdown based on the provided type value.

        :param type_value: The movie type to be selected (e.g., 'Movie', 'Series').
        """
        logger = get_logger()
        logger.info(f"Clicking on 'Type' dropdown to select: {type_value}")
        self.wait_and_click(self.type_dropdown)
        dropdown_option = (By.XPATH,
                           f"//p[text()='Type']//following::div[1]//div/div/div[starts-with(@id, 'react-select') and text()='{type_value}']")
        self.wait_and_click(dropdown_option)
        logger.info(f"'{type_value}' selected from 'Type' dropdown.")

    def click_select_genre_dropdown(self, genre_value):
        """
        Selects a genre from the 'Genre' dropdown based on the provided genre value.

        :param genre_value: The genre to be selected (e.g., 'Action', 'Drama').
        """
        logger = get_logger()
        logger.info(f"Clicking on 'Genre' dropdown to select: {genre_value}")
        self.wait_and_click(self.genre_dropdown)
        dropdown_option = (By.XPATH,
                           f"//p[text()='Genre']//following::div[1]//div/div/div[starts-with(@id, 'react-select') and text()='{genre_value}']")
        self.wait_and_click(dropdown_option)
        logger.info(f"'{genre_value}' selected from 'Genre' dropdown.")

    def click_select_start_year_dropdown(self, start_year_val):
        """
        Selects the start year from the 'Year' dropdown based on the provided value.

        :param start_year_val: The start year to be selected (e.g., '2000').
        """
        logger = get_logger()
        logger.info(f"Clicking on 'Start Year' dropdown to select: {start_year_val}")
        self.wait_and_click(self.start_year_dropdown)
        dropdown_option = (By.XPATH,
                           f"//p[text()='Year']//following::div[2]//div/div/div[starts-with(@id, 'react-select') and text()='{start_year_val}']")
        self.wait_and_click(dropdown_option)
        logger.info(f"'{start_year_val}' selected as start year.")

    def click_select_end_year_dropdown(self, end_year_val):
        """
        Selects the end year from the 'Year' dropdown based on the provided value.

        :param end_year_val: The end year to be selected (e.g., '2024').
        """
        logger = get_logger()
        logger.info(f"Clicking on 'End Year' dropdown to select: {end_year_val}")
        self.wait_and_click(self.end_year_dropdown)
        dropdown_option = (By.XPATH,
                           f"//span[@class='text-white mx-2']/following-sibling::div//div/div/div[starts-with(@id, 'react-select') and text()='{end_year_val}']")
        self.wait_and_click(dropdown_option)
        logger.info(f"'{end_year_val}' selected as end year.")

    def set_start_end_year(self, start_year, end_year):
        """
        Selects the start and end year from their respective dropdowns.

        :param start_year: Year to select as start year.
        :param end_year: Year to select as end year.
        """
        logger=get_logger()
        logger.info(f"Setting start year to: {start_year}")
        self.click_select_start_year_dropdown(start_year)
        time.sleep(3)

        logger.info(f"Setting end year to: {end_year}")
        self.click_select_end_year_dropdown(end_year)
        time.sleep(3)

    def set_value_for_type_genre(self, dropdown_label, dropdown_value):
        """
        Sets the value for either 'Type' or 'Genre' dropdowns based on the label provided.

        :param dropdown_label: Label of the dropdown ('Type' or 'Genre').
        :param dropdown_value: Value to be selected from the dropdown.
        """
        logger = get_logger()
        logger.info(f"Setting dropdown '{dropdown_label}' with value: {dropdown_value}")
        if dropdown_label == 'Type':
            self.click_select_type_dropdown(dropdown_value)
        elif dropdown_label == 'Genre':
            self.click_select_genre_dropdown(dropdown_value)
        else:
            logger.warning(f"Unsupported dropdown label: {dropdown_label}")
        time.sleep(3)

    def validate_entire_movie_list(self):
        """
        Validates the entire movie list across all pagination pages.
        For each movie card, it checks if the image (src), movie name,
        genre, and year are correctly displayed. If any detail is missing,
        the test will assert with an appropriate error message.
        """
        logger = get_logger()
        logger.info("Starting validation of the entire movie list...")

        page_number = self.get_driver().find_element(
            By.XPATH, "//div[@id='react-paginate']//li[position()=last()-1]/a"
        ).text
        logger.info(f"Total number of pages found: {page_number}")

        for i in range(1, int(page_number)):
            time.sleep(3)
            logger.info(f"Validating movie list on page {i}...")

            list_tile = self.get_driver().find_elements(
                By.XPATH, "//div[@class='flex flex-col items-center']"
            )

            for movie_detail in list_tile:
                # self.wait_for(movie_detail)
                self.get_driver().execute_script("arguments[0].scrollIntoView(true);", movie_detail)

                src_value = movie_detail.find_element(By.XPATH, ".//img").get_attribute('src')
                movie_name = movie_detail.find_element(
                    By.XPATH, ".//p[@class='text-blue-500 font-bold py-1']"
                ).text
                desc_name = movie_detail.find_element(
                    By.XPATH, ".//p[@class='text-gray-500 font-light text-sm']"
                ).text

                # Parse genre and year
                genre_name, year = "", ""
                if ", " in desc_name:
                    parts = desc_name.split(", ")
                    if len(parts) >= 2:
                        genre_name = parts[0]
                        year = parts[1]

                # Validation
                if src_value == '':
                    logger.error(f"Movie Tile is missing for {movie_name}")
                    assert False, f"Movie Tile is missing for {movie_name}"
                if movie_name == '':
                    logger.error("Movie Name is missing")
                    assert False, "Movie Name is missing"
                if genre_name == '':
                    logger.error(f"Movie Genre is missing for {movie_name}")
                    assert False, f"Movie Genre is missing for {movie_name}"
                if year == '':
                    logger.error(f"Movie Year is missing for {movie_name}")
                    assert False, f"Movie Year is missing for {movie_name}"

                logger.info(f"Validated movie: {movie_name}, Genre: {genre_name}, Year: {year}")

            self.wait_and_click(self.next_page)
            logger.info("Navigated to next page.")

    def validate_movie_genre(self, genre_type):
        """
        Validates that all listed movies match the specified genre across all paginated pages.

        Args:
            genre_type (str): The expected genre to be validated against each movie tile.

        Raises:
            AssertionError: If any movie's genre does not match the expected genre.
        """
        logger = get_logger()
        logger.info(f"Validating movie genres across pages. Expected genre: {genre_type}")

        page_number = self.get_driver().find_element(By.XPATH,
                                                     "//div[@id='react-paginate']//li[position()=last()-1]/a").text
        for i in range(1, int(page_number)):
            time.sleep(3)
            logger.debug(f"Processing page {i} of {page_number}")
            list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")
            for movie_detail in list_tile:
                self.get_driver().execute_script("arguments[0].scrollIntoView(true);", movie_detail)
                movie_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-blue-500 font-bold py-1']").text
                desc_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-gray-500 font-light text-sm']").text

                # Parse genre
                genre_name = ""
                if ", " in desc_name:
                    parts = desc_name.split(", ")
                    if len(parts) >= 2:
                        genre_name = parts[0]

                logger.debug(f"Movie: {movie_name}, Genre found: {genre_name}")
                if genre_name != genre_type:
                    logger.error(f"Genre mismatch for movie: {movie_name}. Expected: {genre_type}, Found: {genre_name}")
                    assert False, f"Movie Genre is mismatching for {movie_name}. Expected is {genre_type} but actual is {genre_name}"

            self.wait_and_click(self.next_page)
            logger.info(f"Navigated to next page after validating page {i}")

    def validate_movie_year_range(self, start_year, end_year):
        """
        Validates that all the movies listed between paginated pages fall within the specified year range.

        Args:
            start_year (str): The starting year for movie filtering.
            end_year (str): The ending year for movie filtering.

        Raises:
            AssertionError: If any movie's release year is outside the specified start and end year range.
        """
        logger = get_logger()
        logger.info(f"Validating movies between year range {start_year} and {end_year}")
        start = int(start_year)
        end = int(end_year)

        page_number = self.get_driver().find_element(By.XPATH,
                                                     "//div[@id='react-paginate']//li[position()=last()-1]/a").text
        logger.info(f"Total number of pages found: {page_number}")

        for i in range(1, int(page_number)):
            time.sleep(3)
            logger.info(f"Validating movies on page {i}")
            list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")

            for movie_detail in list_tile:
                self.get_driver().execute_script("arguments[0].scrollIntoView(true);", movie_detail)
                movie_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-blue-500 font-bold py-1']").text
                desc_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-gray-500 font-light text-sm']").text

                # Parse genre and year
                genre_name, year = "", ""
                if ", " in desc_name:
                    parts = desc_name.split(", ")
                    if len(parts) >= 2:
                        year = parts[1]

                logger.info(f"Validating year '{year}' for movie '{movie_name}'")
                # Validation
                if int(year) < start or int(year) > end:
                    logger.error(f"Movie '{movie_name}' with year {year} is outside the range {start}-{end}")
                    assert False, f"Movie year {year} is not within the filter range {start}-{end} for {movie_name}."

            logger.info("Clicking on next page button")
            self.wait_and_click(self.next_page)

    def valid_rating(self, rate: str):
        """
        Validates and applies the rating on the UI based on the provided value.

        Args:
            rate (str): Rating value in string format (e.g., "3.0", "4.5")

        Raises:
            AssertionError: If the rating is not a valid number or does not meet required conditions.
        """
        logger=get_logger()
        logger.info(f"Validating rating: {rate}")
        try:
            value = rate.split('.')[0]
            value = int(value)
            rating_value = Decimal(rate)
        except Exception as e:
            logger.error(f"Invalid rating input: {rate}. Exception: {str(e)}")
            assert False, 'Rating must be a valid number'

        if rating_value == 0 or rating_value > 5:
            logger.error(f"Rating {rate} is out of valid range (0.5 - 5.0)")
            assert False, 'Please provide a valid Rating between 0.5 and 5.0'

        if rate.endswith(".0"):
            logger.info(f"Rating ends with .0, selecting full star at position {value}")
            star_type = 'rc-rate-star-second'
            single_star = self.get_driver().find_element(By.XPATH,
                                                         f"//p[text()='Ratings']/following-sibling::ul/li[{value}]//div[@class='{star_type}']")
            self.hover_click(single_star)
            logger.info(f"Clicked on full star rating for {rate}")
            return

        elif rate == "0.5":
            logger.info("Rating is 0.5, selecting first half star")
            star_type = 'rc-rate-star-first'
            half_star = self.get_driver().find_element(By.XPATH,
                                                       f"//p[text()='Ratings']/following-sibling::ul/li[{value}]//div[@class='{star_type}']")
            self.hover_click(half_star)
            logger.info("Clicked on 0.5 star rating")
            return

        elif rate.endswith(".5"):
            value = value + 1
            logger.info(f"Rating ends with .5, selecting half star at position {value}")
            star_type = 'rc-rate-star-second'
            half_star = self.get_driver().find_element(By.XPATH,
                                                       f"//p[text()='Ratings']/following-sibling::ul/li[{value}]//div[@class='{star_type}']")
            self.hover_click(half_star)
            logger.info(f"Clicked on half star rating for {rate}")
            return

        else:
            logger.error(f"Invalid rating format provided: {rate}")
            assert False, 'Please provide a rating ending with .0 or .5 (e.g., 3.0, 4.5)'

    def capture_rated_list(self):
        time.sleep(3)
        global rated_movies
        rated_movies = []

        list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")
        for movie_detail in list_tile:
            self.get_driver().execute_script("arguments[0].scrollIntoView(true);", movie_detail)
            src_value = movie_detail.find_element(By.XPATH, ".//img").get_attribute('src')
            movie_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-blue-500 font-bold py-1']").text
            rated_movies.append(movie_name)
            desc_name = movie_detail.find_element(By.XPATH, ".//p[@class='text-gray-500 font-light text-sm']").text
            # Parse genre and year
            genre_name, year = "", ""
            if ", " in desc_name:
                parts = desc_name.split(", ")
                if len(parts) >= 2:
                    genre_name = parts[0]
                    year = parts[1]
            # Validation
            if src_value == '':
                assert False, f"Movie Tile is missing for {movie_name}"
            if movie_name == '':
                assert False, "Movie Name is missing"
            if genre_name == '':
                assert False, f"Movie Genre is missing for {movie_name}"
            if year == '':
                assert False, f"Movie Year is missing for {movie_name}"

        return rated_movies

    def compare_star_rated_movies(self, first_star, second_star):
        self.valid_rating(first_star)
        first_star_list = self.capture_rated_list()

        self.valid_rating(second_star)
        second_star_list = self.capture_rated_list()

        common_values = list(set(first_star_list) & set(second_star_list))

        if common_values != '':
            assert False, f"{first_star} star rated & {second_star} star rated movies are having {common_values} movie list "

    def click_category_link(self, category_name):
        category_mapping = {
            'Popular': self.popular_link,
            'Trend': self.trend_link,
            'Newest': self.newest_link,
            'Top rated': self.top_rated_link,
        }
        locator = category_mapping.get(category_name)
        if locator:
            self.wait_and_click(locator)
        else:
            raise ValueError(f"Unknown category: {category_name}")

    def verify_category_link_highlight(self, category_name):
        # Wait until the highlighted element is present and has 'text-white' class
        self.wait_for(self.highlight_text)
        class_value = self.get_driver().find_elements(By.XPATH, "//ul[@class='list-none flex']/li")
        for highlighted_txt in class_value:
            if 'text-white' in highlighted_txt.get_attribute('class'):
                actual_link = highlighted_txt.find_element(By.XPATH, ".//a").text
                assert actual_link == category_name, f"{category_name} link is not highlighted"

    def get_total_pages(self):
        self.wait_for(self.last_page_num)
        global total_page_count
        page_number = self.get_driver().find_element(By.XPATH,
                                                     "//div[@id='react-paginate']//li[position()=last()-1]/a").text
        total_page_count= int(page_number)

    def validate_pagination_and_movies(self):

        for i in range(total_page_count):
            self.wait_for(self.movie_tile)
            list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")
            if len(list_tile)==0:
                assert False, f'Movie list tile is not present in {i} page'
            self.wait_and_click(self.next_page)
            self.wait_for(self.next_page)
            self.wait_for(self.wait_spin)

    def validate_pagination_nxt_prev(self, num):
        enter_count=int(num)
        if enter_count<total_page_count:
            for i in range(enter_count):
                self.wait_for(self.movie_tile)

                # Validate movie tiles are present
                list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")
                assert len(list_tile) > 0, f"Movie list tile is not present on page {i + 1}"

                # If not on the last page, try navigating
                if i < enter_count - 1:
                    # Click next
                    self.wait_and_click(self.next_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)

                    # Click previous (go back to original page)
                    self.wait_and_click(self.prev_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)

                    # Click next again (to progress to the next page in loop)
                    self.wait_and_click(self.next_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)
        else:
            raise ValueError(f"Entered page number {num} is more than the current page number")

    def validate_pagination_descending(self, num):
        enter_count = int(num)
        range_count=total_page_count-enter_count
        if enter_count < total_page_count:
            for i in range(total_page_count, range_count, -1):

                self.wait_and_click(self.last_page_num)
                self.wait_for(self.movie_tile)

                # Validate movie tiles are present
                list_tile = self.get_driver().find_elements(By.XPATH, "//div[@class='flex flex-col items-center']")
                assert len(list_tile) > 0, f"Movie list tile is not present on page {i - 1}"

                # If not on the last page, try navigating
                if i < enter_count + 1:
                    # Click previous (go back to original page)
                    self.wait_and_click(self.prev_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)

                    # Click next
                    self.wait_and_click(self.next_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)

                    # Click previous (go back to original page)
                    self.wait_and_click(self.prev_page)
                    self.wait_for(self.next_page)
                    self.wait_for(self.wait_spin)
        else:
            raise ValueError(f"Entered page number {num} is more than the current page number")

