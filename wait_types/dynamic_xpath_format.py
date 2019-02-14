from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DynamicXPathFormat():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseUrl)
        hw = HandyWrappers(driver)

        # Go on the Login page
        elementSignIn = hw.isElementPresent("//a[contains(text(),'Login')]", By.XPATH)
        if elementSignIn:
            elementSignIn.click()
        # Do login
        elementEmailAddress = hw.isElementPresent("user_email", By.ID)
        if elementEmailAddress:
            elementEmailAddress.send_keys("test@email.com")
        elementPassword = hw.isElementPresent("user_password", By.ID)
        if elementPassword:
            elementPassword.send_keys("abcabc")
        elementLogIn = hw.isElementPresent("commit", By.NAME)
        if elementLogIn:
            elementLogIn.click()

        # Search for Java
        elementSeachLogedIn = hw.isElementPresent("search-courses", By.ID)
        if elementSeachLogedIn:
            elementSeachLogedIn.send_keys("Java")
        elementDoSeachLogedIn = hw.isElementPresent("search-courses-button", By.ID)
        if elementDoSeachLogedIn:
            elementDoSeachLogedIn.click()


dxf = DynamicXPathFormat()
dxf.test()
