import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import time
from Pages import AmazonMainPage


class MainPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.openSite = AmazonMainPage.MainPage(cls.driver)
        cls.driver.maximize_window()

    def setUp(self):
        self.openSite.sign_in_site()

    def test_simple_test(self):
        pass

    def tearDown(self):
        time.sleep(4)
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
