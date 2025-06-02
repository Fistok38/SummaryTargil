from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartContentsPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_icon = (By.XPATH, "//a[@id='cart-icon-bubble']")
        self.product_name = (By.XPATH, "//a[@class='cart-item__name h4 break']")
        self.product_quantity = (By.XPATH, "//input[@class='quantity__input']")
        self.product_price = (By.XPATH, "//span[@class='price price--end']")

    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def verify_cart_contents(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_name)
        )

        name = self.driver.find_element(*self.product_name).text
        quantity = self.driver.find_element(*self.product_quantity).get_attribute("value")
        price = self.driver.find_element(*self.product_price).text

        assert name != "", "Product name is empty"
        assert int(quantity) > 0, "Quantity should be greater than 0"
        assert "₪" in price or price.strip() != "", "Price is not displayed properly"