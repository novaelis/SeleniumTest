from selenium import webdriver
import time

class FindByClassTag():

    def test(self):
        """ It didn't want to find by tag name so i used xpath to find specific input field"""

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseURL)

        elementByClassName = driver.find_element_by_class_name("inputs")
        elementByClassName.send_keys("Proba")

        if elementByClassName is not None:
            print('We found element by Displayed Class')

        #elementByTagName = driver.find_element_by_tag_name("input")
        elementByTagName = driver.find_element_by_xpath("//*[@id='displayed-text']")
        elementByTagName.send_keys("Nesto")

        elementByTagName2 = driver.find_element_by_tag_name("h1")
        elementByTagName2_text = elementByTagName2.text

        if elementByTagName is not None:
            print('We found element by Tag Name')

        if elementByTagName2 is not None:
            print('We found element by Tag Name2', elementByTagName2_text)

        time.sleep(10)

find = FindByClassTag()
find.test()