from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class HiddenElements():

    def testLetsKodeIt(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        elementHideShowTextBox = driver.find_element(By.ID, "displayed-text")
        # Find the state of the text box
        stateHideSnowTextBox = elementHideShowTextBox.is_displayed()  # True if visible, False if hidden
        # Exception if not presented in the DOM

        print("{0} visibility is {1}".format(elementHideShowTextBox.get_attribute('name'), stateHideSnowTextBox))
        time.sleep(2)

        # Click the Hide button
        elementHideTextBox = driver.find_element(By.ID, "hide-textbox")
        elementHideTextBox.click()
        print("{0} visibility is {1}".format(elementHideShowTextBox.get_attribute('name'),
                                             elementHideShowTextBox.is_displayed()))
        time.sleep(2)

        # Clik the Show button
        elementSnowTextBox = driver.find_element(By.ID, "show-textbox")
        elementSnowTextBox.click()

        # Find the stae of the text box
        print("{0} visibility is {1}".format(elementHideShowTextBox.get_attribute('name'),
                                             elementHideShowTextBox.is_displayed()))
        time.sleep(2)
        # Browser Close
        driver.close()

    def testExpedia(self):
        baseUrl = "https://expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(1)

        elementsFlights = driver.find_element(By.CSS_SELECTOR, "#tab-flight-tab-hp")
        elementsFlights.click()

        elementOneWayTrip = driver.find_element(By.ID, "flight-type-one-way-label-hp-flight")
        elementOneWayTrip.click()

        elementReturningTrip = driver.find_element(By.ID, "flight-returning-hp-flight")
        print("Is Returning Trip visible?", elementReturningTrip.is_displayed())

        driver.close()


he = HiddenElements()
he.testLetsKodeIt()
he.testExpedia()
