from selenium import webdriver
import time

class RadioButtonsAndCheckboxes():

    def isEnabled(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        bmwRadioBtn = driver.find_element_by_id("bmwradio")
        bmwRadioBtn.click()

        time.sleep(2)

        benzRadioBtn = driver.find_element_by_id("benzradio")
        benzRadioBtn.click()

        time.sleep(2)

        bmwCheckbox = driver.find_element_by_id("bmwcheck")
        bmwCheckbox.click()

        time.sleep(2)

        benzCheckbox = driver.find_element_by_id("benzcheck")
        benzCheckbox.click()

        print("bmwRadioBtn is selected? ", bmwRadioBtn.is_selected())
        print("benzRadioBtn is selected? ", benzRadioBtn.is_selected())
        print("bmwCheckbox is selected? ", bmwCheckbox.is_selected())
        print("bmwCheckbox is selected? ", benzCheckbox.is_selected())


rbac = RadioButtonsAndCheckboxes()
rbac.isEnabled()