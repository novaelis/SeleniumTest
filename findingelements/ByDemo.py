from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseURL = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)

        elementById = driver.find_element(By.ID, "name")

        if elementById is not None:
            print("We found an element by Id")

        elementByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if elementByXpath is not None:
            print("We found an element by XPath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "a[href*=sign_in]")

        if elementByCSS is not None:
            print("We found an element by CSS_SELECTOR AND WILDCARD" + elementByCSS.text)

        elementExercise = driver.find_element(By.XPATH, "//td[contains(text(),'30')]")
        elementExercise = driver.find_element(By.XPATH, "//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td")
        print('price of Python Programming Language is: '+ str(elementExercise.text))

        driver.get("https://dhtmlx.com/docs/products/dhtmlxGrid/samples/02_clipboard/01_grid_selection.html")

        elementExercise2 = driver.find_element(By.XPATH,"//div[@id='gridbox']//td[@title='The Green Mile']/following-sibling::td[1]")


demo = ByDemo()
demo.test()
