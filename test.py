# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
#
# assert "Python" in driver.title
#
# elem = driver.find_element_by_name("q")
#
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
#
# assert "No results found." not in driver.page_source
#
# # driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import base64


class GetText():

    def test(self):
        baseUrl = "https://tracking-game.reaktor.com/signal/vs/noise/play"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get(baseUrl)

        elementOpenText = driver.find_element(By.XPATH, "//div[@class='puzzle']")
        text = elementOpenText.text
        # print("Text is: ", text)

        textForInspect = text[text.find('.....................') + 25:text.find('TRANSMIT SUCCESSFUL')]
        print(text.find('.....................'), text.find('TRANSMIT SUCCESSFUL'))
        print(textForInspect)
        textWithResult = []
        for letter in textForInspect:
            if len(textWithResult) < 16:
                if letter in textWithResult:
                    textWithResult.clear()
                    textWithResult.append(letter)
                    continue
            else:
                break
            textWithResult.append(letter)
            # print(textWithResult)

        word = ''.join(textWithResult)
        encoded_word = base64.b64decode(word)
        print(encoded_word.decode('ascii'))

        elementTypePassword = driver.find_element(By.ID, "answer")
        elementTypePassword.send_keys(encoded_word.decode('ascii'))

        elementSubmit = driver.find_element(By.ID, "submit")
        elementSubmit.click()


gt = GetText()
gt.test()
