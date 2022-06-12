from Locators import Locators
from Common.CustomFind import Find


class LoginSection():
    def __init__(self, driver):
        self.driver = driver
        self.locators = Locators.LocatorsClass()
        self.Find = Find.FindElement(self.driver)

    def input_email_or_number(self, argument):
        emailSection = self.Find.customFind(self.locators.emailSectionLocator)
        emailSection.click()
        emailSection.send_keys(argument)

    def press_to_continue_button(self):
        continueButton = self.Find.customFind(self.locators.continueButtonLocator)
        continueButton.click()
