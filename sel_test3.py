from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#21.28936399229375

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.XPATH, '//input[@type="text"]')
    
    # заполнить все текстовые поля за 20 секунд
    for element in elements:
        element.send_keys("a")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

