from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_btn = (By.ID, "ProductSubmitButton-template--17101875839199__main")
        self.cart_icon = (By.XPATH, "//a[@id='cart-icon-bubble']")

    def open_product_page(self, url):
        self.driver.get(url)

    def click_add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_btn)
        ).click()



    def is_cart_icon_visible(self):
        WebDriverWait(self.driver, 10)
        return self.driver.find_element(*self.cart_icon).is_displayed()
