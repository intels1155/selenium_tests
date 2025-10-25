from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # ----
    submitButton = browser.find_element(By.XPATH, '//button[@type="submit"]')
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))

    #button = document.getElementsByTagName("button")[0];
    browser.execute_script("return arguments[0].scrollIntoView(true);", submitButton)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robotCheckbox.click()

    robotRadioButton = browser.find_element(By.ID, "robotsRule")
    robotRadioButton.click()

    #submitButton = browser.find_element(By.XPATH, '//button[@type="submit"]')
    submitButton.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
