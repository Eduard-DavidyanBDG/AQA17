from selenium.webdriver.common.by import By
import random


class LocatorsClass():
    # Sign in
    moveToButton = (By.ID, "nav-link-accountList-nav-line-1")
    emailSectionLocator = (By.ID, "ap_email")
    continueButtonLocator = (By.ID, "continue")
    passwordSectionLocator = (By.ID, "ap_password")
    submitButtonLocator = (By.ID, "signInSubmit")

    # Product Search
    searchFieldLocator = (By.ID, "twotabsearchtextbox")
    # Choose product
    chooseProduct = (By.XPATH, "(//img[@class = 's-image'])[46]")
    # {random.randint(1, 48)}

    # Add to cart button
    addToCartButtonLocator = (By.ID, "add-to-cart-button")

    # Cart Section
    cartButtonLocator = (By.ID, "nav-cart-count-container")
    cartCount = (By.ID, "nav-cart-count")

    deleteButtonLocator = (By.XPATH, "(//input[@class = 'a-color-link'])[1]")
    # (By.LINK_TEXT, "Delete")

    # Your Profiles
    yourProfiles = (By.XPATH, "(//h2[@class = 'a-spacing-none ya-card__heading--rich a-text-normal'])[6]")
    manageYourProfiles = (By.ID, "home-profile-0")

    namePencil = (By.ID, "name-edit-pencil-image")
    nameChangeLine = (By.ID, "profile-name-text-input")
    saveChangesButton = (By.ID, "profile-name-edit-submit-button")

    # Sign Out Button
    signOutButtonLocator = (By.ID, "nav-item-signout")