from Pages.cart_page import CartPage
from Pages.cart_contents_page import CartContentsPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_cart_full_flow(driver):
    # שלב 1: כניסה לעמוד מוצר והוספה לעגלה
    cart_page = CartPage(driver)
    cart_page.open_product_page(
        "https://www.thebear.co.il/products/%D7%98%D7%91%D7%9C%D7%99%D7%95%D7%AA-%D7%A4%D7%95%D7%A8%D7%9E%D7%95%D7%9C"
        "%D7%94-2-%D7%9C%D7%A0%D7%A9%D7%99%D7%9D-%D7%9C%D7%AA%D7%9E%D7%99%D7%9B%D7%94-%D7%91%D7%92%D7%95%D7%A3-%D7%A9"
        "%D7%9C%D7%9A-%D7%9C%D7%90%D7%95%D7%A8%D7%9A-%D7%9B%D7%9C-%D7%94%D7%99%D7%95%D7%9D-%D7%9E%D7%97%D7%99%D7%A8"
        "-%D7%94%D7%A9%D7%A7%D7%AA-%D7%9E%D7%95%D7%A6%D7%A8-%D7%97%D7%93%D7%A9")
    cart_page.click_add_to_cart()

    # שלב 2: פתיחת העגלה ואימות פרטים ראשוניים
    cart_contents = CartContentsPage(driver)
    cart_contents.open_cart()
    cart_contents.verify_cart_contents()

    # שלב 3: שינוי כמות ל-2
    quantity_input = driver.find_element(By.XPATH, "//input[@class='quantity__input']")
    quantity_input.clear()
    quantity_input.send_keys("2")

    try:
        update_btn = driver.find_element(By.NAME, "update")
        update_btn.click()
    except:
        pass  # יתכן שהעדכון קורה אוטומטית
    time.sleep(5)

    # שלב 4: אימות שסכום כולל מופיע
    total_selector = (By.XPATH, "//span[@class='price price--end']")
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(total_selector)
    )
    total = driver.find_element(*total_selector).text
    assert "₪" in total or total.strip() != "", "Updated total price is missing"

    #  שלב 5: לחיצה על כפתור 'לקופה'
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "CartDrawer-Checkout"))
    )
    checkout_button.click()

    #  שלב 6: המתנה לטעינת עמוד קופה
    WebDriverWait(driver, 10).until(
        EC.url_contains("checkouts")
    )
    assert "checkouts" in driver.current_url.lower(), "Checkout page did not load"

    # שלב 7: מילוי פרטי לקוח
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "email"))
    )
    time.sleep(2)
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.XPATH, "//input[@placeholder='שם פרטי']").send_keys("משה")
    driver.find_element(By.XPATH, "//input[@placeholder='שם משפחה']").send_keys("כהן")
    driver.find_element(By.XPATH, "//input[@placeholder='חברה (אופציה)']").send_keys("מוטורולה")
    driver.find_element(By.XPATH, "//input[@placeholder='עיר']").send_keys("תל אביב")
    driver.find_element(By.XPATH, "//input[@placeholder='כתובת']").send_keys("גולמוב")
    driver.find_element(By.XPATH, "//input[@placeholder='דירה, קומה, מספר']").send_keys("בניין 4 דירה 2")
    driver.find_element(By.XPATH, "//input[@placeholder='מספר טלפון']").send_keys("0546703888")
    driver.find_element(By.ID, "sms_marketing_opt_in").click()

    # שלב 8: הכנסת קופון


    coupon_input = driver.find_element(By.XPATH, "//input[@name='reductions']")
    coupon_input.clear()
    coupon_input.send_keys("Stair8")

    # לחץ על APPLY

    apply_button = driver.find_element(By.XPATH,"//section[@class='_1fragem1y _1fragemm8']//button[@type='submit']")
    apply_button.click()

    #שלב 9 : אימות שההנחה התקבלה
    success_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//strong[contains(text(),'בהזמנה זו חסכת')]"))
    )
    assert success_msg.text or "בהזמנה זו חסכת" in success_msg.text, "Coupon success message not shown"

    clear_button = driver.find_element(By.XPATH, "//div[@id='tag-0']//button[@type='button']")
    clear_button.click()
    coupon_input = driver.find_element(By.XPATH, "//input[@name='reductions']")
    coupon_input.send_keys("Stair")
    apply_button = driver.find_element(By.XPATH, "//section[@class='_1fragem1y _1fragemm8']//button[@type='submit']")
    apply_button.click()

    fail_msg = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-for-ReductionsInput0"))
    )
    assert fail_msg.text or "Enter a valid discount code" in fail_msg.text, "Coupon success message not shown"

    driver.find_element(By.XPATH, "//input[@placeholder='שם פרטי']").clear()
    firstname = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "error-for-TextField0"))
    )
    assert firstname.text or "Enter a first name" in firstname.text, "first name is mandatory"



