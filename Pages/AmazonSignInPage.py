from Locators import Locators
from Common.CustomFind import Find


class SignInPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Find.FindElement(self.driver)
        self.locator = Locators.LocatorsClass()

    def sign_in(self):
        signInButton = self.find.customFind(self.locator.moveToButton)
        signInButton.click()
