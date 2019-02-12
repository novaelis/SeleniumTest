from selenium import webdriver
from pprint import pprint

class BrowserInteractions():

    def test(self):

        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()

        #Window Maximize
        driver.maximize_window()
        #Open the Url
        driver.get(baseURL)
        #Get Title
        title = driver.title
        print("Title of the web page is: "+title)
        #Get Current Url
        current_url = driver.current_url
        print("Current Url of the web page is: ", current_url)
        #Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(current_url)
        print("Browser Refreshed 2st time")
        #Open another Url
        driver.get("https://sso.teachable.com/secure/42299/users/sign_in?clean_login=true&reset_purchase_session=1")
        current_url = driver.current_url
        print("Current Url of the web page is: ", current_url)
        #Browser Back
        driver.back()
        print("Go one step back in browser history")
        driver.forward()
        print("Go one step forward in browser history")
        #Get Page Source
        pageSource = driver.page_source
        #Browser Close/Quit
        driver.close()
        driver.quit()
        #pprint(source)

bi = BrowserInteractions()
bi.test()