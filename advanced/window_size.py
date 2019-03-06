from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class WindowSize():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        # driver.maximize_window()
        driver.get(baseUrl)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script(" return window.innerWidth")
        print("Height: " + str(height))
        print("Width: " + str(width))

        driver.quit()


ws = WindowSize()
ws.test()
