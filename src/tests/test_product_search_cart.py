from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from config.config import (
    BASE_URL,
    PRODUCT_NAME
)

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_add_product_to_cart():

    options = Options()

    options.page_load_strategy = "eager"

    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        ),
        options=options
    )

    driver.maximize_window()

    home = HomePage(driver)

    product = ProductPage(driver)

    cart = CartPage(driver)

    try:

        home.open_website(BASE_URL)

        home.search_product(PRODUCT_NAME)

        home.select_product()

        product.add_product_to_cart()

        cart.open_cart()

        cart.verify_product_in_cart()

    finally:

        driver.quit()


if __name__ == "__main__":

    test_add_product_to_cart()