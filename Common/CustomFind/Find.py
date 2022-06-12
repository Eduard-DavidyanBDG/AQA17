from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindElement():
    def __init__(self, driver):
        self.driver = driver

    def customFind(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return element
        except:
            self.driver.save_screenshot("../Common/Screenshots/Screen.png")

            print("ERROR: Page Element not found !!!")
            exit(2)
