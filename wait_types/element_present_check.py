from selenium import webdriver
from utilities.handy_wrappers import HandyWrappers
from selenium.webdriver.common.by import By


class ElementPresentCheck():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)
        hw = HandyWrappers(driver)

        elementState = hw.isElementPresent('name', By.ID)
        print(elementState)
        elementState2 = hw.elementPresenceCheck("//input[@id='name1'", By.XPATH)
        print(elementState2)


epc = ElementPresentCheck()
epc.test()
