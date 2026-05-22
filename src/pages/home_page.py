'''
Created on 22-May-2026

@author: Raut
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 20)

    SEARCH_ICON = (
        By.CSS_SELECTOR,
        "[aria-label='Search']"
    )

    SEARCH_BOX = (
        By.ID,
        "cmdk-input"
    )
    
    PRODUCT_LINK = (
       (By.CSS_SELECTOR,
         ".product-media")
    )

    # Open the website
    
    def open_website(self, url):

        self.driver.get(url)

    def search_product(self, product_name):

        search_icon = self.wait.until(
            EC.presence_of_element_located(
                self.SEARCH_ICON
            )
        )

        self.driver.execute_script(
            "arguments[0].click();",
            search_icon
        )

        search_box = self.wait.until(
            EC.visibility_of_element_located(
                self.SEARCH_BOX
            )
        )

        search_box.send_keys(product_name)

        search_box.send_keys(Keys.ENTER)

    def select_product(self):
            
        product = self.wait.until(
            EC.element_to_be_clickable(
                self.PRODUCT_LINK
            )
        )

        product.click()