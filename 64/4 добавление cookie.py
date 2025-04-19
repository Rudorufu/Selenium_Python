# ➕ Добавьте cookie на сайт.
#
# 🔹 Задача: Помогите Пряне попасть на сайт
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Установите cookie с именем "secretKey" и значением "selenium123".
#     3️⃣ Обновите страницу. Если всё сделано правильно, появится пароль в элементе с id="password".
#     4️⃣ Извлеките пароль .text
#     5️⃣ Вставьте пароль в поле ниже, между кавычками.
#

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://parsinger.ru/selenium/6/6.3.3/index.html'

cookie_dict = {
    'name': 'secretKey',    # Любое имя для cookie
    'value': 'selenium123',  # Любое значение для cookie
}

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.add_cookie(cookie_dict)
    browser.refresh()
    txt = browser.find_element(By.ID, 'password').text
    print(txt)