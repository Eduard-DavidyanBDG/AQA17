from Locators import Locators
from Common.CustomFind import Find
from selenium.webdriver.common.action_chains import ActionChains


class SignOutClass():
    def __init__(self, driver):
        self.driver = driver
        self.find = Find.FindElement(self.driver)
        self.locator = Locators.LocatorsClass()

    def move_to_sign_out(self):
        MoveToButton = self.find.customFind(self.locator.moveToButton)
        action = ActionChains(self.driver)
        action.move_to_element(MoveToButton).perform()

    def click_to_sign_out_button(self):
        PressToSignOutButton = self.find.customFind(self.locator.signOutButtonLocator)
        PressToSignOutButton.click()
