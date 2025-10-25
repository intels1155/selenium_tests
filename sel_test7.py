from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element(By.ID, "num1")
x = int(x_element.text)

y_element = browser.find_element(By.ID, "num2")
y = int(y_element.text)

sum = x + y


select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum)) # ищем элемент с текстом "Python"

submitButton = browser.find_element(By.XPATH, '//button[@type="submit"]')
submitButton.click()

time.sleep(30)
#keyboard.wait('esc')
# закрываем браузер
browser.close()
time.sleep(2)
browser.quit()

