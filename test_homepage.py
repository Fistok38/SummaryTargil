def test_homepage_loads(driver):
    driver.get("https://www.thebear.co.il/")
    assert "מוצרי הרבלייף במחירים מעולים| ®THE BEAR | משלוח עד הבית בחינם – The Bear" in driver.title or driver.find_element("css selector", "header")

def test_logo_appears(driver):
    driver.get("https://www.thebear.co.il/")
    logo = driver.find_element("css selector", "img[alt='The Bear']")
    assert logo.is_displayed()

