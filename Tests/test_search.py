from Pages.search_actions import SearchActions

def test_search_snack(driver):
    driver.get("https://www.thebear.co.il/products/%D7%98%D7%91%D7%9C%D7%99%D7%95%D7%AA-%D7%A4%D7%95%D7%A8%D7%9E%D7"
               "%95%D7%9C%D7%94-2-%D7%9C%D7%A0%D7%A9%D7%99%D7%9D-%D7%9C%D7%AA%D7%9E%D7%99%D7%9B%D7%94-%D7%91%D7%92%D7"
               "%95%D7%A3-%D7%A9%D7%9C%D7%9A-%D7%9C%D7%90%D7%95%D7%A8%D7%9A-%D7%9B%D7%9C-%D7%94%D7%99%D7%95%D7%9D-%D7"
               "%9E%D7%97%D7%99%D7%A8-%D7%94%D7%A9%D7%A7%D7%AA-%D7%9E%D7%95%D7%A6%D7%A8-%D7%97%D7%93%D7%A9/")
    search = SearchActions(driver)
    search.locate_search_bar()
    search.type_search_term("חטיף")
    search.submit_search()
    assert search.verify_results("חטיף"), "המילה 'חטיף' לא נמצאה בתוצאות החיפוש"