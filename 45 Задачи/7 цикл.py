# 🔽 Операция: Выпадающие списки
#
# Приветствую, агенты-разработчики! Сегодня наша миссия — "Операция 'Выпадающие списки'".
# В этой операции мы сталкиваемся с нечто большим, чем просто чек-боксы или текстовые поля.
# Мы имеем дело с выпадающим списком, содержащим ключи к секретному хранилищу данных.
# Задачи
#
#     Вход в Кодовую Комнату: Откройте сайт с помощью Selenium.
#     Извлечение Ключей: Получите значения всех элементов выпадающего списка.
#     Дешифровка Кода: Сложите (плюсуйте) все извлеченные значения.
#     Использование Кода: Вставьте получившийся результат в поле на сайте и нажмите кнопку.
#     Получение Конечного Результата: Копируйте длинное число, которое появится после нажатия на кнопку.
#
# Работа с выпадающими списками практически ничем не отличается от работы с чек-боксами или полями.
#
# Для того, чтобы получить значение любого элемента из выпадающего списка, мы можем использовать привычные нам методы поиска элемента.
#
#  В нашем случае, на нашем сайте все элементы выпадающего списка могут быть спокойно найдены по тегу.
#  Метод By.TAG_NAME нам в этом поможет.
#


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/7/7.html') # Откройте сайт с помощью Selenium
    list_of_options = browser.find_elements(By.TAG_NAME, 'option') # Получите значения всех элементов выпадающего списка.
    sums = 0
    for i in list_of_options:
        sums += int(i.text) # Сложите (плюсуйте) все извлеченные значения.
    browser.find_element(By.ID, 'input_result').send_keys(sums) # Вставьте получившийся результат в поле на сайте и
    browser.find_element(By.ID, 'sendbutton').click() # нажмите кнопку.
    print(browser.find_element(By.ID, 'result').text) # Копируйте длинное число, которое появится после нажатия на кнопку

