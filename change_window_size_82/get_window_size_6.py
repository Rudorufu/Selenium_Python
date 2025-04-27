# ➕ Сумма размеров окна браузера.
#
# 🔹 Задача: Получить секретный пароль через правильное вычисление суммы размеров окна браузера.
#
#     1️⃣ С помощью Selenium зайдите на сайт-тренажер.
#     2️⃣ Получите размеры окна браузера.
#     3️⃣ Сложите значения.
#     4️⃣ Введите полученную сумму в поле на сайте тренажере и нажмите кнопку «Проверить».
#     5️⃣ Если ответ верный (с учетом небольшого допуска), на странице отобразится секретный пароль.
#     6️⃣ Вставьте пароль в поле ниже на степик.
#
# 🟢 Внимание: данный тренажёр работает только через Selenium.


from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://parsinger.ru/selenium/8/8.2.2/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    size = browser.get_window_size()
    # width = browser.get_window_size('width')
    size = size['width'] + size['height']
    print(size)
    browser.find_element(By.ID, 'answer').send_keys(size)
    browser.find_element(By.ID, 'checkBtn').click()
    print(browser.find_element(By.ID, 'resultMessage').text)