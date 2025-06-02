from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.shakes_link = (By.LINK_TEXT, "טבליות")
        self.product_link = (By.XPATH, "//div[@id='ProductGridContainer']//h3[@id='title-template--17101875314911__product-grid-8846095876319']")
        self.product_title = (By.XPATH, "//div[@class='product__title']")
        self.product_image = (By.XPATH, "//img[@src='//www.thebear.co.il/cdn/shop/files/2_87607b85-d660-441e-9b44-02a29d4f15e8.jpg?v=1731067484&width=1946']")
        self.product_price = (By.XPATH, "//span[@class='price-item price-item--sale price-item--last']")

    def navigate_to_shakes_category(self):
        self.driver.get("https://www.thebear.co.il/")
        self.driver.find_element(*self.shakes_link).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.product_link)
        )

    def click_on_any_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.product_link)
        ).click()

    def verify_title_image_price(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_title)
        )
        assert self.driver.find_element(*self.product_title).is_displayed(), "Product title not displayed"
        assert self.driver.find_element(*self.product_image).is_displayed(), "Product image not displayed"
        assert self.driver.find_element(*self.product_price).is_displayed(), "Product price not displayed"
