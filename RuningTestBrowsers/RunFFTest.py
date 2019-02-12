from selenium import webdriver

class RunFFTest():

    def testMethod(self):

        driver = webdriver.Firefox()
        driver.get("http://google.com")

ff = RunFFTest()
ff.testMethod()