from selenium import webdriver

class RunChromeTest():

    def testMethod(self):

        driver = webdriver.Chrome()
        driver.get("http://google.com")

ff = RunChromeTest()
ff.testMethod()