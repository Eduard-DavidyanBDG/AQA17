import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from Common.Variables import Variables
from Pages import AmazonSignInPage
from Pages import AmazonMainPage
from Pages import EmailSection
from Pages import PasswordSection
from Pages import SelectProductPage
from Pages import AddToCartPage
from Pages import CartSection
import time


class SearchProductClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.mainPage = AmazonMainPage.MainPage(cls.driver)
        cls.pressToSignInButton = AmazonSignInPage.SignInPageClass(cls.driver)
        cls.emailSection = EmailSection.LoginSection(cls.driver)
        cls.passwordSection = PasswordSection.LoginSection(cls.driver)
        cls.variables = Variables.ProjectVariables()
        cls.selectProduct = SelectProductPage.SelectProductClass(cls.driver)
        cls.addToCart = AddToCartPage.AddToCartClass(cls.driver)
        cls.cart = CartSection.DeleteProduct(cls.driver)
        cls.driver.maximize_window()

    def setUp(self):
        self.driver.get(self.mainPage.variable.mainUrl)

    def test_search_Product(self):
        # Sign to search
        self.pressToSignInButton.sign_in()
        self.driver.implicitly_wait(10)
        self.emailSection.input_email_or_number(self.variables.signInEmail)
        # time.sleep(1)
        self.emailSection.press_to_continue_button()
        self.driver.implicitly_wait(10)
        # time.sleep(1.5)
        self.passwordSection.input_password(self.variables.signInPassword)
        time.sleep(2)
        self.passwordSection.press_to_submit_button()
        # Starting search
        self.mainPage.input_product()
        self.driver.implicitly_wait(10)
        # Find Product
        self.selectProduct.select_product()
        # Add to Cart
        self.driver.implicitly_wait(10)
        self.addToCart.add_to_cart()
        self.driver.implicitly_wait(10)
        # Open Cart Section And Deleting Products
        self.cart.open_cart_section()
        self.driver.implicitly_wait(10)
        time.sleep(2)
        self.cart.delete_all_products()

    def tearDown(self):
        time.sleep(4)
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
