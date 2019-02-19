from selenium import webdriver
from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        self.locatorType = locatorType.lower()
        if self.locatorType == "id":
            return By.ID
        elif self.locatorType == 'name':
            return By.NAME
        elif self.locatorType == "xpath":
            return By.XPATH
        elif self.locatorType == "css":
            return By.CSS_SELECTOR
        elif self.locatorType == "classname":
            return By.CLASS_NAME
        elif self.locatorType == "linktext":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + "not correct/supported")
        return False

    def getElement(self, locator, locatorType='id'):
        # element = None
        try:
            element = self.driver.find_element(self.getByType(locatorType), locator)
            print("Element found.")
        except:
            print("Element not found")
        return element

    def isElementPresent(self, locator, locatorType):
        try:
            element = self.driver.find_element(locatorType, locator)
            if element is not None:
                return element
            else:
                return False
        except:
            print("Element not found")
            return False

    def elementPresenceCheck(self, locator, locatorType):
        try:
            elementList = self.driver.find_elements(locatorType, locator)
            if len(elementList) > 0:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False
