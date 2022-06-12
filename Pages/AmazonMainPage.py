from Common.Variables import Variables
from Common.CustomFind import Find
from Locators import Locators
from selenium.webdriver.common.keys import Keys


class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.variable = Variables.ProjectVariables()
        self.find = Find.FindElement(self.driver)
        self.locator = Locators.LocatorsClass()

    def sign_in_site(self):
        self.driver.get(self.variable.mainUrl)

    def input_product(self):
        searchField = self.find.customFind(self.locator.searchFieldLocator)
        searchField.click()
        searchField.send_keys(self.variable.productName)
        searchField.send_keys(Keys.ENTER)
