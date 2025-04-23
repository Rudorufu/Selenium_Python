# 🖱️ Применяем double_click().
#
# 🔹 Задача: учимся даблкликать по элементу.
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Выполните двойной клик по заданному элементу, чтобы получить пароль в виде фразы.
#     3️⃣ Извлеките текст пароля из появившегося элемента с id="password" и вставьте его в поле ниже между кавычками.
#
# 🟢Внимание даблклик сработает только через Selenium.
#
#  Важно: Обычный одиночный клик не сработает! Не пытайтесь обмануть систему.
#  Два последовательных вызова метода click() не генерируют событие dblclick, которое слушается в JavaScript.
#
# Используйте двойной клик (double_click). 🖱️➡️🖱️


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
url = "https://parsinger.ru/selenium/7/7.3.2/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    actions = ActionChains(browser)
    double_click_area = browser.find_element(By.ID, 'dblclick-area')
    actions.double_click(double_click_area).perform()
    print(browser.find_element(By.ID, 'password').text)