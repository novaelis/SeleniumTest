from selenium import webdriver

class FindByIdName():

    def test(self):

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseURL)

        elementByID = driver.find_element_by_id("name")
        elementByID_text = elementByID.text
        elementByID_attribute_value = elementByID.get_attribute('value')

        if elementByID is not None:
            print('We found element by ID', elementByID_text)

        elementByName = driver.find_element_by_name("show-hide")
        elementByName_text = elementByName.text
        elementByName_attribute_value = elementByName.get_attribute('value')

        if elementByName is not None:
            print('We found element by Name', elementByName_text)

find = FindByIdName()
find.test()