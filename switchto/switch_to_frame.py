from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToFrame():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.execute_script("window.scrollBy(0, 1500);")

        # Switch to frame using Id
        # driver.switch_to.frame("courses-iframe")
        # Switch to frame using name
        # driver.switch_to.frame(driver.find_element(By.NAME, "iframe-name"))
        # driver.switch_to.frame("iframe-name")
        # Switch to frame using numbers
        # driver.switch_to.frame(0)
        # Search course

        driver.find_element(By.ID, "search-courses").send_keys("Python")
        driver.find_element(By.ID, "search-course-button").click()
        time.sleep(3)

        # Switch back to the parent handle

        # driver.switch_to.parent_frame()
        driver.switch_to.default_content()
        driver.execute_script("window.scrollBy(0, -1500);")
        time.sleep(3)
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(3)


stf = SwitchToFrame()
stf.test()
