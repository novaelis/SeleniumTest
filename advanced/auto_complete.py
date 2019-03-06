from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class AutoComplete():

    def test1(self):
        baseUrl = "http://southwest.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        # Send Partial Data

        time.sleep(5)
        # Find the item and click

        time.sleep(3)
        driver.quit()


ac = AutoComplete()
ac.test1()
