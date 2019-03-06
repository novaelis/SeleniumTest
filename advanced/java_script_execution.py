from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class JavaScriptExecution():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        # driver.get(baseUrl)
        # javascript version
        driver.execute_script("window.location = '{0}';".format(baseUrl))

        # element = driver.find_element(By.ID, "name")
        # javascript version
        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys("Test")

        time.sleep(5)


jse = JavaScriptExecution()
jse.test()
