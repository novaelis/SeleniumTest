from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SwitchToWindow():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        # Find parent handle -> Main Window
        parentHandle = driver.current_window_handle
        print(parentHandle)

        # Find open window button and click it
        driver.find_element(By.ID, "openwindow").click()
        time.sleep(2)
        # Find all handles, there should be two handles clicking open window button
        handles = driver.window_handles
        for handle in handles:
            print("Handle is: ", handle)

        # Switch to window and search course
        driver.switch_to.window(handles[1])
        driver.find_element(By.ID, "search-courses").send_keys("python")
        time.sleep(2)

        # Switch back to the parent handle
        driver.switch_to.window(handles[0])
        time.sleep(2)

        # driver.find_element(By.ID, "openwindow").click()
        # driver.find_element(By.ID, "search-courses").send_keys("python")
        # it now working because selenium stay on default first page


stw = SwitchToWindow()
stw.test()
