from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

import time


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
        elementDoSeachLogedIn = hw.isElementPresent("search-course-button", By.ID)
        if elementDoSeachLogedIn:
            elementDoSeachLogedIn.click()

        time.sleep(2)

        # Goes through list of courses and click on every choice

        # elementSeleniumWithJava = hw.isElementPresent("//div[contains(text(),'Selenium WebDriver With Java')]",
        #                                               By.XPATH)
        # if elementSeleniumWithJava:
        #     elementSeleniumWithJava.click()
        # driver.back()
        print('Krece sa listom')
        listOfCourse = ['Selenium WebDriver With Java', 'JavaScript', 'Step', 'WebDriver Bundle']
        for elementTitle in listOfCourse:
            print("//div[contains(text(),'{0}')]".format(elementTitle))
            element = hw.isElementPresent("//div[contains(text(),'{0}')]".format(elementTitle), By.XPATH)
            # If existed then clikc on element
            if element:
                element.click()
            else:
                print(element)
            # Wait before browser goes back
            time.sleep(2)
            driver.back()

        time.sleep(1000)


dxf = DynamicXPathFormat()
dxf.test()
