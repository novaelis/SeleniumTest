from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from wait_types.explicit_wait_type import ExplicitWaitType
import time


class ExplicitWaitDemo3():

    def test(self):
        baseUrl = 'https://global.cheapflights.com/'
        driver = webdriver.Firefox()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)
        ewt = ExplicitWaitType(driver)

        # SETUP Flyting from, Flying to, Deparing and Returning date, number of adults
        # Flying to
        # driver.find_element(By.XPATH, "//input[@name='destination']").send_keys("DOH")

        # elementFlyingTo = ewt.waitForElement("//input[@name='destination']", 'xpath')
        # elementFlyingTo.send_keys("DOH")
        ewt.waitForElement("//input[@name='destination']", 'xpath').send_keys("DOH")

        # elementFlyingTo = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='destination'")))
        # elementFlyingTo.send_keys("DOH")
        # Click on destination list Flying to

        # elementDOH = wait.until(EC.presence_of_element_located((By.ID, "ap-DOH/15839")))
        # elementDOH.click()

        # elementDOH = ewt.waitForElement("ap-DOH/15839", 'id')
        # elementDOH.click()
        ewt.waitForElement("ap-DOH/15839").click()

        # Type date for departing
        # elementDepartingDate = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR,
        #      "div[aria-label='Departure date input']")))
        # elementDepartingDate.send_keys("Tue 2/19")
        # elementDepartingData = ewt.waitForElement("div[aria-label='Departure date input']", 'css')
        # elementDepartingData.send_keys("Tue 2/19")
        ewt.waitForElement("div[aria-label='Departure date input']", 'css').send_keys("Tue 2/19")
        # Select depart date
        # elementSelectDepart = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'February 19')]//div[text()='19']")))
        # elementSelectDepart.click()
        # elementSelectDepart = ewt.waitForElement("//div[contains(@aria-label,'February 19')]//div[text()='19']",'xpath')
        # elementSelectDepart.click()
        ewt.waitForElement("//div[contains(@aria-label,'February 19')]//div[text()='19']", 'xpath').click()
        # Type date for returning
        # driver.find_element(By.XPATH,
        #                     "//div[@class='fieldBlock dateBlock col-field col-date single-date-picker']//div[text()='Return']").send_keys(
        #     "Wed 3/6")
        # Type date for returning
        # elementReturnDate = wait.until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR,
        #      "div[aria-label='Return date input']")))
        # elementReturnDate.send_keys("Wed 3/6")
        # elementReturnDate = ewt.waitForElement("div[aria-label='Return date input']",'css')
        time.sleep(2)
        # Trying to click on specific returnin date so list can disappear so we can clik on Find deals
        # elementSelectReturn = wait.until(
        #     EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'March 6')]//div[text()='6']")))
        # elementSelectReturn = ewt.waitForElement("//div[contains(@aria-label,'March 6')]//div[text()='6']", 'xpath')
        ewt.waitForElement("//div[contains(@aria-label,'March 6')]//div[text()='6']", 'xpath').click()
        # elementSelectDate.click()
        # elementSelectDate.click() not working so trying down statment
        # driver.execute_script("arguments[0].click();", elementSelectReturn)
        time.sleep(2)
        # clicking on h2 so list can disappear
        # driver.find_element(By.XPATH,
        #                     "//div[contains(@class,'flightsVisible')]").click()
        # elementClickOnH2 = ewt.waitForElement("//div[contains(@class,'flightsVisible')]",'xpath')
        # elementClickOnH2.click()
        ewt.waitForElement("//div[contains(@class,'flightsVisible')]", 'xpath').click()
        # Click on Find deals button
        # elementFindDeals = wait.until(EC.presence_of_element_located(
        #     (By.XPATH, "//div[@class='fieldBlock buttonBlock']//button[@type='submit']")))
        # elementFindDeals.click()
        # elementFindDeals = ewt.waitForElement("//div[@class='fieldBlock buttonBlock']//button[@type='submit']",'xpath')
        # elementFindDeals.click()
        ewt.waitForElement("//div[@class='fieldBlock buttonBlock']//button[@type='submit']", 'xpath').click()
        time.sleep(5)
        # driver.close()
        # Exit popup screen
        # driver.find_element(By.XPATH, "//label[contains(text(),'Same')])]").click()
        # elementSameDeparting = wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Same')]")))
        # elementSameDeparting = wait2.until(
        #     EC.element_to_be_clickable((By.ID, "qual-show-departing-returning-airport")))
        # elementSameDeparting.click()
        # elementSameDeparting = ewt.waitForElement("//label[contains(text(),'Same')]",'xpath')
        # elementSameDeparting.click()
        ewt.waitForElement("//label[contains(text(),'Same')]", 'xpath', 20).click()


ewd = ExplicitWaitDemo3()
ewd.test()
