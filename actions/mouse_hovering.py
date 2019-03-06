from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class MouseHovering():

    def test(self):
        baseUrl = 'https://learn.letskodeit.com/p/practice'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.execute_script("window.scrollBy(0,700);")
        time.sleep(2)

        elementMouseHover = driver.find_element(By.ID, "mousehover")

        try:
            actions = ActionChains(driver)
            actions.move_to_element(elementMouseHover).click_and_hold().perform()
            print("Mouse Hovered on element")
            time.sleep(2)
            elementTopLink = driver.find_element(By.XPATH, "//div[@class='mouse-hover-content']//a[text()='Top']")
            actions.move_to_element(elementTopLink).click().perform()
            print("Item Clicked")
            time.sleep(2)
        except:
            print("Mouse Hover failed on element")


mh = MouseHovering()
mh.test()
