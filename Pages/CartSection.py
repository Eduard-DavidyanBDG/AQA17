import time
from Locators import Locators
from Common.CustomFind import Find


class DeleteProduct():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators.LocatorsClass()
        self.find = Find.FindElement(self.driver)

    def open_cart_section(self):
        openSection = self.find.customFind(self.locator.cartButtonLocator)
        openSection.click()

    def delete_one_product(self):
        deleteButton = self.find.customFind(self.locator.deleteButtonLocator)
        deleteButton.click()

    def delete_all_products(self):
        cartItemsCount = self.find.customFind(self.locator.cartCount)
        cartItemsCount = int(cartItemsCount.text)
        for i in range(cartItemsCount):
            self.delete_one_product()
            time.sleep(2)
