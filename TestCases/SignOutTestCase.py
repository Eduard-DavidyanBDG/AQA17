import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Common.Variables import Variables
from Pages import AmazonSignInPage
from Pages import AmazonMainPage
from Pages import EmailSection
from Pages import PasswordSection
from Pages import SignOutPage

import time


class SearchProductClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.mainPage = AmazonMainPage.MainPage(cls.driver)
        cls.pressToSignInButton = AmazonSignInPage.SignInPageClass(cls.driver)
        cls.emailSection = EmailSection.LoginSection(cls.driver)
        cls.passwordSection = PasswordSection.LoginSection(cls.driver)
        cls.signOut = SignOutPage.SignOutClass(cls.driver)
        cls.variables = Variables.ProjectVariables()
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self.mainPage.variable.mainUrl)

    def test_search_Product(self):
        # Sign to search
        self.pressToSignInButton.sign_in()
        time.sleep(2)
        self.emailSection.input_email_or_number(self.variables.signInEmail)
        time.sleep(1)
        self.emailSection.press_to_continue_button()
        time.sleep(2)
        self.passwordSection.input_password(self.variables.signInPassword)
        time.sleep(2)
        self.passwordSection.press_to_submit_button()
        self.driver.implicitly_wait(10)
        self.signOut.move_to_sign_out()
        self.driver.implicitly_wait(10)
        self.signOut.click_to_sign_out_button()

    def tearDown(self):
        time.sleep(4)
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
