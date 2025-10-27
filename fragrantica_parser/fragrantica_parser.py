import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

# w i p
'''
данные для извлечения:
 + бренд brand

 + название Name ()
 //*[@id="toptop"]/h1/text()
  split по brand

 + пол m / f / u (match-case)

 + аккорды: массив строк, произвольное количество элементов

 - пирамида нот (массивы строк)
  - верхние
  - средние
  - базовые
 
 - стойкость (среднее от 1 до 5) 
 - шлейф (среднее от 1 до 4)
 - пол по голосам ( f fu u um m )

 - Вывод собранных данных в файл
'''

# ссылки для открытия в браузере
link1 = "https://www.fragrantica.ru/perfume/Mandarina-Duck/Freedomland-61390.html"
link2 = "https://www.fragrantica.ru/perfume/Dilis-Parfum/Frozen-Morning-116553.html"

# запуск браузера и webdriver
browser = webdriver.Chrome()

# открыть ссылку
browser.get(link1)

# получить бренд
brand_name_element = browser.find_element(By.XPATH, '//*[@itemprop="brand"]//span')
brand_name = brand_name_element.text
print(brand_name)

# получить название
title_element = browser.find_element(By.XPATH, '//*[@id="toptop"]/h1')
title_extracted = title_element.text # получена строка, включающая название, бренд, пол
#print(title_extracted)

title = title_extracted.split(brand_name)[0].strip() # оставить только название
print(title)

# пол
parf_gender_element = browser.find_element(By.XPATH, '//*[@id="toptop"]/h1/small')
parf_gender = parf_gender_element.text

match parf_gender:
    case "для женщин":
        parf_gender = "f"
    case "для мужчин":
        parf_gender = "m"
    case _:
        parf_gender = "u"

print(parf_gender)

# аккорды
accords_array = [] # 
accord_elements = browser.find_elements(By.CLASS_NAME, "accord-bar") # найти все элементы с аккордами
for element in accord_elements:
    accords_array.append(element.text)
print("Аккорды: ", accords_array)

# ноты: !!! устранить дублирование кода---
#   верхние
top_notes_array = []
top_notes_elements = browser.find_elements(
    By.XPATH, 
    '//*[@id="pyramid"]//div[contains(@class, "notes-box")]/following-sibling::div[1]//*[text()]')
for element in top_notes_elements:
    top_notes_array.append(str(element.text))
print("Верхние ноты: ", top_notes_array)
# //*[@id="pyramid"]//*[text()]
# //*[@id="pyramid"]/div[1]//text()

# найти 3 div с нотами
# //*[@id="pyramid"]//div[contains(@class, "notes-box")]/following-sibling::div

# вытаскивает все ноты из трех div
# //*[@id="pyramid"]//div[contains(@class, "notes-box")]/following-sibling::div//*[text()]

#   средние
middle_notes_array = []
middle_notes_elements = browser.find_elements(
    By.XPATH, 
    '//*[@id="pyramid"]//div[contains(@class, "notes-box")]/following-sibling::div[2]//*[text()]')
for element in middle_notes_elements:
    middle_notes_array.append(str(element.text))
print("Средние ноты", middle_notes_array)

#   базовые
base_notes_array = []
base_notes_elements = browser.find_elements(
    By.XPATH, 
    '//*[@id="pyramid"]//div[contains(@class, "notes-box")]/following-sibling::div[3]//*[text()]')
for element in base_notes_elements:
    base_notes_array.append(str(element.text))
print("Базовые ноты", base_notes_array)

keyboard.wait('esc')
browser.close()
# time.sleep(2)
browser.quit()