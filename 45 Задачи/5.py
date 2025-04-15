# 🔒 Операция кодовый замок
#
# Добро пожаловать, агенты!
# Сегодня перед нами стоит задача не просто извлечь данные, но и взаимодействовать с интерфейсом веб-сайта,
# чтобы добраться до скрытой информации.
# Представьте, что перед вами замок с комбинацией в виде чек-боксов.
#
#
# Задачи
#
#     Взлом Кодового Замка: Откройте веб-сайт с помощью Selenium.
#     Активация Чек-боксов: Найдите все чек-боксы на странице и установите их в положение checked с помощью .click().
#     Открывание Секрета: Как только все чек-боксы будут активированы, нажмите на кнопку.
#     Доступ к Секретным Данным: Скопируйте число, которое появится в теге <p id="result">Result</p>.


from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('http://parsinger.ru/selenium/4/4.html') # Откройте веб-сайт с помощью Selenium.
    boxes = browser.find_elements(By.CLASS_NAME, 'check') # Найдите все чек-боксы на странице
    for i in boxes:
        i.click() # установите их в положение checked с помощью .click().
    browser.find_element(By.CLASS_NAME, 'btn').click() # Как только все чек-боксы будут активированы, нажмите на кнопку.
    result = browser.find_element(By.ID, 'result').text # Скопируйте число, которое появится в теге <p id="result">Result</p>.
    print(result)
