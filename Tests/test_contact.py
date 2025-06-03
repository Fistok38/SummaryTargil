from Pages.contact import Contact
from selenium.webdriver.common.by import By
import time
def test_contact_page(driver):
    driver.get("https://www.thebear.co.il/products/%D7%98%D7%91%D7%9C%D7%99%D7%95%D7%AA-%D7%A4%D7%95%D7%A8%D7%9E%D7"
               "%95%D7%9C%D7%94-2-%D7%9C%D7%A0%D7%A9%D7%99%D7%9D-%D7%9C%D7%AA%D7%9E%D7%99%D7%9B%D7%94-%D7%91%D7%92%D7"
               "%95%D7%A3-%D7%A9%D7%9C%D7%9A-%D7%9C%D7%90%D7%95%D7%A8%D7%9A-%D7%9B%D7%9C-%D7%94%D7%99%D7%95%D7%9D-%D7"
               "%9E%D7%97%D7%99%D7%A8-%D7%94%D7%A9%D7%A7%D7%AA-%D7%9E%D7%95%D7%A6%D7%A8-%D7%97%D7%93%D7%A9")
    contact = Contact(driver)
    contact.scroll_to_bottom()
    contact.click_contact_link()
    assert contact.verify_contact_page_loaded(), "Contact page did not load as expected"

    fullName = driver.find_element(By.ID,"ContactForm-name")
    fullName.send_keys("בדיקה אוטומציה")
    email = driver.find_element(By.ID,"ContactForm-email")
    email.send_keys("automation@hackeru.com")
    phone = driver.find_element(By.ID,"ContactForm-phone")
    phone.send_keys("054667232")
    messgae = driver.find_element(By.ID,"ContactForm-body")
    messgae.send_keys("כיף ללמוד אוטומציה עם דניאל")
    time.sleep(2)
    driver.find_element(By.XPATH,"//div[@class='contact__button']/button[@type='submit']").click()