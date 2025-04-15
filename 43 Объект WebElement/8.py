# 1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
# 2️⃣ Найдите кнопку по id со значением "secret-key-button".
# 3️⃣ Кликните по кнопке.
# 4️⃣ Извлеките значение атрибута data с помощью метода .get_attribute("data").
# 5️⃣ Вставьте полученный ключ в поле ниже между кавычек.

from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.4/index.html')
    browser.find_element(By.ID, "secret-key-button").click()
    text = browser.find_element(By.ID, "secret-key-button").get_attribute("data")
    browser.quit()
    print(text)