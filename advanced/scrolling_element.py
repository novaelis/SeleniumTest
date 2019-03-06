from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ScrollingElement():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(2)

        # Scroll Element Into View
        element = driver.find_element(By.ID, "mousehover")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -150);")

        # Native Way To Scroll Element Into View
        time.sleep(2)
        driver.execute_script("window.scrollBy(0, -1000);")
        location = element.location_once_scrolled_into_view
        print("Location: " + str(location))
        driver.execute_script("window.scrollBy(0, -150);")


se = ScrollingElement()
se.test()
