from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class Sliders():

    def test(self):
        baseUrl = 'https://jqueryui.com/slider'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        elementSlider = driver.find_element(By.CSS_SELECTOR, "#slider span")
        elementSlideTo = driver.find_element(By.ID, "slider")

        try:
            actions = ActionChains(driver)
            # actions.move_to_element(elementSlider).drag_and_drop_by_offset(elementSlideTo,0,100).perform()
            # simplier solution
            actions.drag_and_drop_by_offset(elementSlider, 100, 0).perform()
            print("Sliding Element Successful")
            time.sleep(4)
        except:
            print("Unsuccessful sliding")

        time.sleep(2)


sl = Sliders()
sl.test()
