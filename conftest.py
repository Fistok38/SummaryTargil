import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.thebear.co.il/")
    yield driver
    driver.quit()

def test_logo_appears(driver):
    driver.get("https://www.thebear.co.il/")
    logo = driver.find_element("css selector", "img[alt='The Bear']")
    assert logo.is_displayed()

