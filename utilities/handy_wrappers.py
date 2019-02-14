from selenium import webdriver
from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        self.locatorType = locatorType.lower()
        if self.locatorType == "id":
            return By.ID
        elif self.locatorType == "xpath":
            return By.XPATH
        else:
            return False

    def getElement(self, locator, locatorType='id'):
        element = None
        try:
            element = self.driver.find_element(self.getByType(locatorType), locator)
            print("Element found.")
        except:
            print("Element not found")
        return element