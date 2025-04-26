# 🆕 Открываем новые вкладки new_window
#
# 🔹 Задача: Открыть 2 вкладки в новом окне, считать их title, преобразовать числа, и вставить полученное число на степик.
#
#     1️⃣ С помощью Selenium запустите сначала браузер с пустой вкладкой about:blank.
#     2️⃣ Используйте метод .new_window("tab") откройте сайт 1 в новой вкладке.
#         3️⃣ Получите из title числовое значение, затем удалите из него все числа 4, 3, 9,  сохраните обработанное число в num1.
#     4️⃣ Откройте сайт 2 в новой вкладке тем же методом.
#         5️⃣ Получите из title числовое значение, затем удалите из него все числа 7, 8, 0,  сохраните обработанное число в num2.
#     6️⃣ Суммируйте полученные ранее числа num1 + num2, полученное значение вставьте в поле ниже на степик.
#
# 🟢Внимание title доступен только через Selenium.
import time

from selenium import webdriver
url = "https://parsinger.ru/selenium/8/8.1/site1/"


with webdriver.Chrome() as browser:
    browser.get("about:blank")
    browser.switch_to.new_window('tab')
    browser.get("https://parsinger.ru/selenium/8/8.1/site1/")
    title = browser.title
    print(title)
    num1 = ''
    for i in title:
        if int(i) not in [4, 3, 9]:
            num1 += i
    print(num1)

    browser.switch_to.new_window('tab')
    browser.get("https://parsinger.ru/selenium/8/8.1/site2/")
    title = browser.title
    print(title)
    num2 = ''
    for i in title:
        if int(i) not in [7, 8, 0]:
            num2 += i
    print(num2)
    print(int(num1) + int(num2))