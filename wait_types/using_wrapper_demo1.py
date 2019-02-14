from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.handy_wrappers import HandyWrappers

class UsingWrappers():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        hw = HandyWrappers(driver)

        element = hw.getElement("name")
        print(element.get_attribute('type'))


uw = UsingWrappers()
uw.test()