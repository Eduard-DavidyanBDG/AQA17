from Locators import Locators
from Common.CustomFind import Find
# from selenium.webdriver.common.action_chains import ActionChains
import names
from selenium.webdriver.common.keys import Keys


class YourAccountClass():
    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators.LocatorsClass()
        self.find = Find.FindElement(self.driver)

    def sign_to_user_account_settings(self):
        profileButton = self.find.customFind(self.locator.moveToButton)
        profileButton.click()
        yourProfiles = self.find.customFind(self.locator.yourProfiles)
        yourProfiles.click()
        # self.driver.implicity_wait(10)
        manageYourProfiles = self.find.customFind(self.locator.manageYourProfiles)
        manageYourProfiles.click()

    def click_to_change_name(self):
        changeName = self.find.customFind(self.locator.namePencil)
        changeName.click()

    def change_name(self):
        nameLine = self.find.customFind(self.locator.nameChangeLine)
        nameLine.clear()
        nameLine.send_keys(names.get_first_name(gender="male"))

    def save_changes(self):
        saveChangesButton = self.find.customFind(self.locator.saveChangesButton)
        saveChangesButton.click()
