# 🖱️ Прокрутка страницы scrollBy.
#
# 🔹 Задача: с помощью Selenium выполните прокрутку страницы.
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Вычислите высоту страницы.
#     3️⃣ Прокрутите страницу на значение, полученное в шаге 2.
#     4️⃣ Извлеките появившийся пароль. Пароль появится в виде текста в элементе с id="secret-container".
#     5️⃣ Вставьте пароль в поле ниже, между кавычками.
#
# 💡 Совет: обязательно добавьте time.sleep() после прокрутки, так как пароль появляется не сразу.
#
# 🟢На сайте установлена защита от ручного скролинга, пароль появиться только при использовании Selenium.
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://parsinger.ru/selenium/7/7.1/index.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    print(browser.find_element(By.ID, 'secret-container').text)