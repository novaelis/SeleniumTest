from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)

        #elementsByClassName = driver.find_elements(By.CLASS_NAME, "btn-style")
        elementsByClassName = driver.find_elements_by_class_name("inputs")

        if elementsByClassName is not None:
            for e in elementsByClassName:
                print("We found an element by Class: ", e.text)

        #elementsByTagName = driver.find_elements(By.TAG_NAME, "legend")
        elementsByTagName = driver.find_elements_by_tag_name("legend")



        if elementsByTagName is not None:
            for e in elementsByTagName:
                print("We found an element by TagName: ", e.text)

        elementByFieldset = driver.find_element(By.CSS_SELECTOR, "fieldset>table")
        print(elementByFieldset)

demo = ListOfElements()
demo.test()
