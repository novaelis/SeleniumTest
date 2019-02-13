from selenium import webdriver

class ElementState():

    def isEnabled(self):
        baseUrl = "http://google.com"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_name("q")
        e1State = e1.is_enabled() # True for enabled and False for disabled
        print("Is E1 is Enabled? -> ", e1State)
        e1.send_keys("letskodeit")

es = ElementState()
es.isEnabled()