from Pages.product_page import ProductPage

def test_product_details_are_displayed(driver):


    product_page = ProductPage(driver)
    product_page.navigate_to_shakes_category()
    product_page.click_on_any_product()
    product_page.verify_title_image_price()


