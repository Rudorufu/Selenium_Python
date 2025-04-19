# 🔙 Переход назад.
#
# 🔹 Задача: перейти на 2 страницы вперёд, затем вернуться назад, используя метод back()и получить код.
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Перейти по ссылке на страницу 2.
#     3️⃣ Перейти по ссылке на страницу 3.
#     4️⃣ Используя метод back(), вернуться на первую страницу и кликнуть по кнопке "Показать код".
#     5️⃣ Пока что вручную скопировать код и вставить его сюда в поле ниже. Позже мы изучим, как работать с Alert окнами с помощью Selenium.
#
# 💡 Совет: добавьте time.sleep() на каждом шаге, чтобы отследить происходящее.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.2/index.html') # Откройте сайт с помощью Selenium
    browser.find_element(By.TAG_NAME, 'a').click()
    browser.find_element(By.TAG_NAME, 'a').click()
    browser.back()
    browser.back()
    browser.find_element(By.ID, 'getPasswordBtn').click()
    time.sleep(20)