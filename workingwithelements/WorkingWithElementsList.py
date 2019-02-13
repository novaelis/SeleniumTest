from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithElementsList():

    def isEnabled(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonsList = driver.find_elements(
            By.XPATH, "//input[contains(@type, 'radio') and contains(@name, 'cars') ]")
        size = len(radioButtonsList)
        print('Size of list of radio buttons is: ', size)

        for rb in radioButtonsList:
            print('Radio buton {0} is selected {1}'.format(rb.get_attribute('value'),rb.is_selected()))

            if not rb.is_selected():
                rb.click()
                time.sleep(2)

wel = WorkingWithElementsList()
wel.isEnabled()