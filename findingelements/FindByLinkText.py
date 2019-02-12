from selenium import webdriver

class FindByXpathCss():

    def test(self):
        """ It won't work in Chrome find_element_by_link_text and find_element_by_partial_link_text
            so i used xpath to find specific elements"""

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        driver.get(baseURL)

        #elementByLinkText = driver.find_element_by_link_text("Login")
        elementByLinkText = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[2]/a")

        if elementByLinkText is not None:
            print('We found element by Link Text')

        #elementByPartialLinkText = driver.find_element_by_partial_link_text("Practice")
        elementByPartialLinkText = driver.find_element_by_xpath("//*[@id='navbar']/div/div/div/ul/li[1]/a")

        if elementByPartialLinkText is not None:
            print('We found element by Partical Link Text')

find = FindByXpathCss()
find.test()