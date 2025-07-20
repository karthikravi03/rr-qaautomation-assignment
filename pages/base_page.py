from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_and_click(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_for(self, locator, timeout=10):
        element=WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return element

    def send_keys(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_driver(self):
        return self.driver

    def hover_click(self, click_elem):
        actions = ActionChains(self.driver)
        actions.move_to_element(click_elem).pause(0.5).move_to_element(click_elem).click().perform()

    def wait_for_dom(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

    def scroll_page_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();",locator)
