from Pages.category_page import CategoryPage

def test_navigate_to_shakes_category(driver):
    category = CategoryPage(driver)
    category.open_homepage()
    category.hover_and_click_shakes()
    category.wait_for_category_page()

    assert "שייקים – The Bear" in driver.page_source or "שייקים – The Bear" in driver.title
