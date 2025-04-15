# 🔍 Поиск внутри списка элементов
#
# 🔹 Задача: прокликать все кнопки в блоках, и получить заветный пароль 🔓.
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Найти все элементы с class="block".
#     3️⃣ Пройтись по каждому элементу в цикле и кликнуть кнопку.
#     4️⃣ После того как все кнопки будут нажаты, появится заветный пароль в теге <password> — считать его с помощью .text.
#     5️⃣ Вставить полученный пароль в поле ниже, между кавычек.


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.2/index.html')
    blocks = browser.find_elements(By.CLASS_NAME, "block")
    for block in blocks:
        block.find_element(By.TAG_NAME,'button').click()
    text = browser.find_element(By.TAG_NAME,'password').text
    browser.quit()
    print(text)
