from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class DropdownSelect():

    def isEnabled(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        selectElement = Select(driver.find_element_by_id("carselect"))

        #Select Benz from drop-down list with index
        selectElement.select_by_index("1")
        time.sleep(2)

        #Select Honda from drop-down list with value
        selectElement.select_by_value("honda")
        time.sleep(2)

        # Select BMW from drop-down list with visible text
        selectElement.select_by_visible_text("BMW")
        time.sleep(2)

        # Select Benz from drop-down list with index
        selectElement.select_by_index(1)
        time.sleep(2)


dds = DropdownSelect()
dds.isEnabled()