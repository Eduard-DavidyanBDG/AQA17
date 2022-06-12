from Locators import Locators
from Common.CustomFind import Find


class LoginSection():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()
        self.Find = Find.FindElement(self.driver)

    def input_password(self, argument):
        passwordSection = self.Find.customFind(self.locators.passwordSectionLocator)
        passwordSection.click()
        passwordSection.send_keys(argument)

    def press_to_submit_button(self):
        submitButton = self.Find.customFind(self.locators.submitButtonLocator)
        submitButton.click()