# Извлеките значение cookie.
#
# 🔹 Задача: вам необходимо найти нужный cookie и извлечь его значение по имени.
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Извлечь значение cookie с name = token_22
#     3️⃣ Вставить в поле ниже, между кавычками.
#
# 💡 Совет: выведите результат в print().


from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.3.1/index.html')
    print(browser.get_cookie('token_22')['value'])