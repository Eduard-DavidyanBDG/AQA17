from Common.CustomFind import Find
from Locators import Locators
from selenium.webdriver.common.keys import Keys


class SelectProductClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Find.FindElement(self.driver)
        self.locator = Locators.LocatorsClass()

    def select_product(self):
        selectProduct = self.find.customFind(self.locator.chooseProduct)
        selectProduct.click()
