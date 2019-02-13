from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.common.keys import Keys
import time

class ClickAndSendKeys():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        sign_in_button_path = "//a[@class='navbar-link fedora-navbar-link']"
        wait = WebDriverWait(driver, 10)
        elementSignIn = wait.until(EC.visibility_of_element_located((By.XPATH, sign_in_button_path)))
#        elementSignIn = driver.find_element(By.XPATH, sign_in_button_path)
        elementSignIn.click()

#        print("Is elementSignIn enabled? ->", elementSignIn.is_enabled())


        elementUsername = driver.find_element(By.ID , "user_email")
        elementUsername.send_keys("test")

        elementPassword = driver.find_element(By.ID, "user_password")
        elementPassword.send_keys("test")

        time.sleep(2)

        elementUsername.clear()

        time.sleep(2)

        elementPassword.clear()



CSK = ClickAndSendKeys()
CSK.test()

