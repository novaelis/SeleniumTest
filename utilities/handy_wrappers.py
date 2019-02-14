from selenium import webdriver
from selenium.webdriver.common.by import By

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    def getStrategy(self, strategy):
        self.strategy = strategy.lower()
        if(self.strategy == "id"):
            return By.ID
        elif(self.strategy == "xpath"):
            return By.XPATH
        else:
            return False

    def getElement(self, locator, strategy='id'):
        element = None
        try:
            element = self.driver.find_element(self.getStrategy(strategy),locator)
            print("Element found.")
        except:
            print("Element not found")
        return element