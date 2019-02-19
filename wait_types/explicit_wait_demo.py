from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys
import time


class ExplicitWaitDemo():

    def test(self):
        baseUrl = 'https://cheapflights.com'
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        wait = WebDriverWait(driver, 10)
        # SETUP Flyting from, Flying to, Deparing and Returning date, number of adults
        # Flying to
        driver.find_element(By.XPATH, "//input[@name='destination']").send_keys("DOH")
        # elementFlyingTo = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='destination'")))
        # elementFlyingTo.send_keys("DOH")
        # Click on destination list Flying to

        elementDOH = wait.until(EC.presence_of_element_located((By.ID, "ap-DOH/15839")))
        elementDOH.click()

        # Type date for departing
        # OVO JE RESENJE ZA https://cheapflights.com
        elementDepartingDate = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             "//div[@class='fieldBlock dateBlock col-field col-date single-date-picker']//div[text()='Depart']")))
        elementDepartingDate.send_keys("Tue 2/19")
        # Select depart date
        elementSelectDepart = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'February 19')]//div[text()='19']")))
        elementSelectDepart.click()
        # Type date for returning
        # driver.find_element(By.XPATH,
        #                     "//div[@class='fieldBlock dateBlock col-field col-date single-date-picker']//div[text()='Return']").send_keys(
        #     "Wed 3/6")
        # Type date for returning
        elementReturnDate = wait.until(EC.presence_of_element_located(
            (By.XPATH,
             "//div[@class='fieldBlock dateBlock col-field col-date single-date-picker']//div[text()='Return']")))
        elementReturnDate.send_keys("Wed 3/6")
        time.sleep(2)
        # Trying to click on specific returnin date so list can disappear so we can clik on Find deals
        elementSelectReturn = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'March 6')]//div[text()='6']")))
        # elementSelectDate.click()
        # elementSelectDate.click() not working so trying down statment
        driver.execute_script("arguments[0].click();", elementSelectReturn)
        time.sleep(2)
        # clicking on h2 so list can disappear
        driver.find_element(By.XPATH,
                            "//div[@class='searchForm flightsForm clearfix']//div[contains(@class,'searchFormWrapper')]//h2").click()
        # Click on Find deals button
        elementFindDeals = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='fieldBlock buttonBlock']//button[@type='submit']")))
        elementFindDeals.click()
        # Exit popup screen
        # driver.find_element(By.XPATH, "//button[contains(@class,'Button-No-Standard-Style close')]").click()
        elementPopUpExit = driver.find_element(By.XPATH, "//button[contains(@class,'Button-No-Standard-Style close')]")


ewd = ExplicitWaitDemo()
ewd.test()
