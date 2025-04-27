# 📐 Настраиваем размер окна.
#
# 🔹 Задача: Настройка размера окна и получение секретного пароля
#
#     1️⃣ С помощью Selenium зайдите на сайт-тренажер.
#     2️⃣ Установите размер окна браузера на 1200×720
#     3️⃣ Нажмите на кнопку "Проверить размер". Если размеры окна установлены корректно (с учетом допустимого отклонения),
#     на странице появится скрытый пароль.
#     4️⃣ Считайте из DOM полученный пароль.
#     5️⃣ Вставьте пароль в поле ниже на степик.


from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://parsinger.ru/selenium/8/8.2.1/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    browser.set_window_size(1200, 720)
    browser.find_element(By.ID, 'checkSizeBtn').click()
    print(browser.find_element(By.ID, 'secret').text)