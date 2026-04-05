'''
Created on 5 Apr 2026

@author: Aniket Kumar
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


AdNabuTestStore_BASE_URL = "https://adnabu-store-assignment1.myshopify.com"
Store_password = "AdNabuQA"
Product_name_To_Search = "snowboard"   # change if needed after checking available products


def setup_driver():
    """Initialize and return Chrome driver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver


def wait_for_element(driver, locator, condition="visible", timeout=10):
    """Reusable explicit wait helper."""
    wait = WebDriverWait(driver, timeout)

    if condition == "visible":
        return wait.until(EC.visibility_of_element_located(locator))
    elif condition == "clickable":
        return wait.until(EC.element_to_be_clickable(locator))
    else:
        raise ValueError("Unsupported wait condition")


def open_homepage(driver):
    """Open store homepage."""
    driver.get(AdNabuTestStore_BASE_URL)


def unlock_store(driver):
    """Enter store password and access the storefront."""
    password_input = wait_for_element(driver, (By.ID, "password"), "visible")
    password_input.clear()
    password_input.send_keys(Store_password)

    enter_button = wait_for_element(driver, (By.XPATH, "//button[contains(.,'Enter')]"), "clickable")
    enter_button.click()


def search_product(driver, product_name):
    """Search for a product from the storefront."""
    search_icon = wait_for_element(
        driver,
        (By.XPATH, "//summary[@aria-label='Search']//span//*[name()='svg'][1]"),
        "clickable"
    )
    search_icon.click()

    search_box = wait_for_element(driver, (By.NAME, "q"), "visible")
    search_box.clear()
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.ENTER)


def open_first_product(driver):
    """Open the first product from search results."""
    first_product = wait_for_element(
        driver,
        (By.XPATH, "//a[@id='CardLink--7801364480090']"),
        "clickable"
    )
    first_product.click()


def add_product_to_cart(driver):
    """Add selected product to cart."""
    add_to_cart_button = wait_for_element(
        driver,
        (By.XPATH, "//button[contains(.,'Add to cart') or contains(.,'Add to Cart')]"),
        "clickable"
    )
    add_to_cart_button.click()


def go_to_cart(driver):
    """Navigate to the cart page."""
    cart_icon = wait_for_element(
        driver,
        (By.XPATH, "//a[contains(@href, '/cart')]"),
        "clickable"
    )
    cart_icon.click()


def verify_cart_has_product(driver):
    """Verify that at least one product exists in the cart."""
    cart_item = wait_for_element(
        driver,
        (By.XPATH, "//a[contains(@href, '/products/')]"),
        "visible"
    )

    assert cart_item.is_displayed(), "Product was not added to cart successfully."


def test_search_and_add_to_cart():
    """Main test: unlock store, search product, add to cart, and verify."""
    driver = setup_driver()

    try:
        open_homepage(driver)
        unlock_store(driver)
        search_product(driver, Product_name_To_Search)
        open_first_product(driver)
        add_product_to_cart(driver)
        go_to_cart(driver)
        verify_cart_has_product(driver)

        print("Test Passed: Search for a product and add it to the cart successfully")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_search_and_add_to_cart()