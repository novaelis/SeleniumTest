from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class CalendarSelection():

    def test1(self):
        baseUrl = "http://expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        # Click flights tab
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        # Find departing field
        elementDepartingField = driver.find_element(By.ID, "flight-departing-hp-flight")
        # Click departing field
        elementDepartingField.click()
        # Find the date to be selected
        elementDepartingDateToSelect = driver.find_element(By.XPATH, "//button[@data-month='1' and @data-day='20']")
        # Click the date
        elementDepartingDateToSelect.click()

        time.sleep(3)
        driver.quit()

    def test2(self):
        baseUrl = "http://expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)
        wait = WebDriverWait(driver, 5, 1)

        # Click flights tab
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element(By.ID, "flight-departing-hp-flight").click()
        # Find all elements from February
        # elementsWithAllFebruaryDates = driver.find_elements(By.XPATH,
        #                                                     "//table[@class='datepicker-cal-weeks']//button[@data-month='1']")
        # for element in elementsWithAllFebruaryDates:
        #     if element.get_attribute("data-day")== '24':
        #         element.click()
        #         break

        elementsWithAllFebruaryDates = driver.find_elements(By.XPATH,
                                                            "//table[@class='datepicker-cal-weeks']//button[@data-month='1']")

        # Select correct February date
        for element in elementsWithAllFebruaryDates:
            if '24' in element.text:
                element.click()
                break
        # Click Returning field
        driver.find_element(By.ID, "flight-returning-hp-flight").click()
        # Find all elements from March
        elementsWithAllMarchDates = driver.find_elements(By.XPATH,
                                                         "//table[@class='datepicker-cal-weeks']//button[@data-month='2']")

        # Select correct March date
        for element in elementsWithAllMarchDates:
            if '22' in element.text:
                element.click()
                break

        # Send text on Flying from
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("Belg")

        # All elements from drop list Flying from

        # elementsFlyingFrom = driver.find_elements(By.XPATH, "//div[@class='display-group-results']//div[@class='multiLineDisplay']")
        elementsFlyingFrom = driver.find_elements(By.XPATH, "//div[@class='display-group-results']//a")
        # elementBelgrade = driver.find_element(By.XPATH, "//div[contains(@class,'multiLineDisplay') ]//b[text()='BEG']")
        # elementBelgrade.click()

        for element in elementsFlyingFrom:
            print(element.get_attribute("data-value"))
            if 'Belgrade' in element.get_attribute("data-value"):
                # element.click()
                driver.execute_script("arguments[0].click()", element)
                break


cs = CalendarSelection()
cs.test2()
