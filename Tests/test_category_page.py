from Pages.category_page import CategoryPage


def test_navigate_to_tablets_category(driver):
    category = CategoryPage(driver)
    category.open_homepage()
    category.hover_and_click_tablets()
    category.wait_for_category_page()

    assert "טבליות – The Bear" in driver.page_source or "טבליות – The Bear" in driver.title


