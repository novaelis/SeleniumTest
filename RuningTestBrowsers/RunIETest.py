from selenium import webdriver

class RunIETest():

    def testMethod(self):

        driver = webdriver.Ie()
        driver.get("http://google.com") 

ff = RunIETest()
ff.testMethod()