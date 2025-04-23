# 🔢 Поиск чисел
#
# Добро пожаловать в удивительный мир веб-скрапинга, где информация иногда прячется в самых неожиданных местах!
# Ваша задача сегодня — вычислить и собрать числа, которые могут появиться на веб-странице.
# Они могут быть ключами к более сложным задачам или даже просто интересным головоломкам.
# Цель
#
#     Инициализация: Откройте заданный веб-сайт с помощью Selenium.
#
#     Обнаружение чекбоксов: На сайте будет 100 чекбоксов. Если кликнуть на чекбокс, может появиться число в теге span
#
#     <span id="result1">954</span>
#
#     Вычисление: Соберите все эти числа и сложите их.
#
#     Отправка ответа: Введите сумму всех чисел, в поле ответа на Stepik.
#
# Заметки и подсказки
#
#     Изучите структуру HTML-страницы, чтобы понять, как Selenium может найти элементы.
#     Будьте осторожны: числа могут появляться и исчезать, поэтому убедитесь, что вы собрали их все.


from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://parsinger.ru/scroll/2/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    checkboxes = browser.find_elements(By.CLASS_NAME, 'checkbox_class')
    for i in checkboxes:
        i.click()
    nums = browser.find_elements(By.TAG_NAME, 'span')
    sums = 0
    for j in nums:
        if j.text.isdigit():
            sums += int(j.text)
    print(sums)