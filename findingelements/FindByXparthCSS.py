from selenium import webdriver

class FindByXpathCss():

    def test(self):

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseURL)

        elementByXpath = driver.find_element_by_xpath("//input[@id='name123']")
        elementByXpath_text = elementByXpath.text
        elementByID_attribute_value = elementByXpath.get_attribute('value')

        if elementByXpath is not None:
            print('We found element by XPATH', elementByXpath_text)

        elementByCss = driver.find_element_by_css_selector("#displayed-text")
        elementByCss_text = elementByCss.text
        elementByName_attribute_value = elementByCss.get_attribute('value')

        if elementByCss is not None:
            print('We found element by Name', elementByCss_text)

find = FindByXpathCss()
find.test()