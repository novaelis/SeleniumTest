from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragAndDrop():

    def test(self):
        baseUrl = 'https://jqueryui.com/droppable'
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseUrl)

        driver.switch_to.frame(0)

        elementToDrag = driver.find_element(By.ID, "draggable")
        elementWhereToDrop = driver.find_element(By.ID, "droppable")
        time.sleep(2)

        try:
            actions = ActionChains(driver)
            # actions.drag_and_drop(elementToDrag,elementWhereToDrop).perform()
            actions.click_and_hold(elementToDrag).move_to_element(elementWhereToDrop).release().perform()
            # I forget perform()!
            print("We draged element: {0}, to element: {1}".format(elementToDrag.text, elementWhereToDrop.text))

        except:
            print("Unsuccessful dragging")

        time.sleep(2)


dad = DragAndDrop()
dad.test()
