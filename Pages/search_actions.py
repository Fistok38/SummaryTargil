from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SearchActions:
    def __init__(self, driver):
        self.driver = driver
        self.search_button = (By.CLASS_NAME, "header__search")
        self.search_input = (By.ID, "Search-In-Modal-1")

    def locate_search_bar(self):

        self.driver.find_element(*self.search_button).click()
        time.sleep(1)

    def type_search_term(self, keyword):

        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(keyword)

    def submit_search(self):

        search_field = self.driver.find_element(*self.search_input)
        search_field.send_keys(Keys.RETURN)
        time.sleep(2)

    def verify_results(self, expected_text):

        return expected_text in self.driver.page_source