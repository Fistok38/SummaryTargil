from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CategoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.top_menu = (By.XPATH, "//ul[@class='list-menu list-menu--inline']")
        self.shakes_link = (By.LINK_TEXT, "שייקים")
        self.category_title = (By.CSS_SELECTOR, ".collection-hero__title")  # Example element to verify page load

    def open_homepage(self):
        self.driver.get("https://www.thebear.co.il/")

    def hover_and_click_shakes(self):
        actions = ActionChains(self.driver)
        top_menu_element = self.driver.find_element(*self.top_menu)
        actions.move_to_element(top_menu_element).perform()
        self.driver.find_element(*self.shakes_link).click()

    def wait_for_category_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.category_title)
        )