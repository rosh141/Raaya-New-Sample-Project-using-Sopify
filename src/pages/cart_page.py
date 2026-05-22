from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    CART_ICON = (
        By.CSS_SELECTOR,
        "[data-testid='cart-icon']"
    )

    CART_TITLE = (
        By.CSS_SELECTOR,
        ".cart-items__title"
    )

    def open_cart(self):

        cart_icon = self.wait.until(
            EC.element_to_be_clickable(
                self.CART_ICON
            )
        )

        cart_icon.click()

    def verify_product_in_cart(self):

        cart_title = self.wait.until(
            EC.visibility_of_element_located(
                self.CART_TITLE
            )
        )

        assert cart_title.is_displayed()

        print("Product added successfully to cart.")