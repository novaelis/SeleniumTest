from selenium import webdriver
from selenium.webdriver.common.by import By


class GetText():

    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        elementOpenTab = driver.find_element(By.ID, "opentab")
        print("Text of {0} is {1}".format(elementOpenTab.get_attribute('id'), elementOpenTab.text))


gt = GetText()
gt.test()
