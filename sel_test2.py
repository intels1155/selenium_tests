import keyboard
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link_1 = "http://suninjuly.github.io/find_link_text"
link_2 = "http://suninjuly.github.io/simple_form_find_task.html"

link_1_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link_1)

    link_to_find = browser.find_element(By.LINK_TEXT, link_1_text)
    link_to_find.click()
    
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

except Exception as error:
    print(f'Произошла ошибка, трэйсбэк: {error}')

finally:
    time.sleep(30)
    keyboard.wait('esc')
    # закрываем браузер
    browser.close()
    time.sleep(2)
    browser.quit()




