from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
import time

class UsingWrappers():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        hw = HandyWrappers(driver)

        element = hw.getElement("name", "Id")
        print(element.get_attribute('type'))
        element2 = hw.getElement("name")
        element2.send_keys("Test")
        time.sleep(2)
        element3 = hw.getElement("//input[@id='name']", "xpath")
        print(element3.get_attribute('type'))

uw = UsingWrappers()
uw.test()