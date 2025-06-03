from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class Contact:
    def __init__(self, driver):
        self.driver = driver
        self.contact_link = (By.LINK_TEXT, "דברו איתנו")

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # ממתין לטעינה מלאה של הפוטר

    def click_contact_link(self):
        """Clicks on the 'דברו איתנו' link"""
        contact_element = self.driver.find_element(*self.contact_link)
        ActionChains(self.driver).move_to_element(contact_element).click().perform()
        time.sleep(2)  # ממתין לטעינת העמוד

    def verify_contact_page_loaded(self):
        """Checks that the contact page loaded by verifying URL or content"""
        return "דברו איתנו" in self.driver.page_source or "contact" in self.driver.current_url