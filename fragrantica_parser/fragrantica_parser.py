import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By

# w i p
'''
данные для извлечения:
 + бренд brand

 + название Name ()
 //*[@id="toptop"]/h1/text()
  резать всё после brand

 -+ пол m / f / u (switch-case)

 + аккорды: массив строк, произвольное количество элементов

 - пирамида нот (массивы строк)
  - верх
  - средние
  - база
 
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
browser.get(link2)

# получить бренд
brand_name_element = browser.find_element(By.XPATH, '//*[@itemprop="brand"]//span')
brand_name = brand_name_element.text
print(brand_name)

# получить название
title_element = browser.find_element(By.XPATH, '//*[@id="toptop"]/h1')
title_extracted = title_element.text # получена строка, включающая название, бренд, пол
print(title_extracted)

title = title_extracted.split(brand_name)[0].strip() # оставить только название
print(title)

# пол
parf_gender_element = browser.find_element(By.XPATH, '//*[@id="toptop"]/h1/small')
parf_gender = parf_gender_element.text
print(parf_gender)

# //*[@id="toptop"]/h1/small

# аккорды
accords_array = []
elements = browser.find_elements(By.CLASS_NAME, "accord-bar") # найти все элементы с акордами
for element in elements:
    accords_array.append(element.text)
print(accords_array)



keyboard.wait('esc')
browser.close()
# time.sleep(2)
browser.quit()