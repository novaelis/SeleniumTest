from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class Screenshots():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        # Go on the Login page
        driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
        # Do login
        driver.find_element(By.ID, "user_email").send_keys("abc@email.com")
        driver.find_element(By.ID, "user_password").send_keys("abcabc")
        driver.find_element(By.NAME, "commit").click()

        self.takeScreenshot(driver)

        # destinationFileName = "C:\\Users\\Dejan Jovanovic\\Documents\\test\\test.png"
        #
        # try:
        #     driver.save_screenshot(destinationFileName)
        #     print(" Screenshot saved to directory --> ::" + destinationFileName)
        # except NotADirectoryError:
        #     print("It's directory issue")
        # except:
        #     print("Screenshots not working.")

    def takeScreenshot(self, driver):
        """
        Takes screenshot og the current open web page
        :param driver:
        :return:
        """

        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "C:\\Users\\Dejan Jovanovic\\Documents\\test"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print(" Screenshot saved to directory --> ::" + destinationFile)
        except NotADirectoryError:
            print("It's directory issue")
        except:
            print("Screebshots not working.")


sc = Screenshots()
sc.test()
