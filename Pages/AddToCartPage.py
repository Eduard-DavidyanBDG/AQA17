from Common.Variables import Variables
from Common.CustomFind import Find
from Locators import Locators


class AddToCartClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Find.FindElement(self.driver)
        self.locator = Locators.LocatorsClass()

    def add_to_cart(self):
        addToCartButton = self.find.customFind(self.locator.addToCartButtonLocator)
        addToCartButton.click()
