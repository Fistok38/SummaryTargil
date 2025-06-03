from Pages.search_actions import SearchActions

def test_search_snack(driver):
    driver.get("https://www.thebear.co.il/")
    search = SearchActions(driver)
    search.locate_search_bar()
    search.type_search_term("חטיף")
    search.submit_search()
    assert search.verify_results("חטיף"), "המילה 'חטיף' לא נמצאה בתוצאות החיפוש"