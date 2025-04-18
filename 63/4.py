# Поиск cookie.
#
# 🔹 Задача: найдите название песни в cookies на сайте, вставить в поле на сайте-тренажере, и получить девиз.
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Получить список всех cookies.
#     3️⃣ Найти название песни.
#     4️⃣ Вставить название в поле для проверки и нажать кнопку «Проверить».
#     5️⃣ Извлечь девиз одного известного персонажа из Dota 2 из элемента с id="result"
#     6️⃣ Вставить девиз в поле ниже, между кавычками.
#
# 💡 Совет: добавляйте time.sleep() как вам удобно, и выведите результат в print().


url = 'https://parsinger.ru/selenium/6/6.3/index.html'
from selenium import webdriver
from selenium.webdriver.common.by import By
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')

with webdriver.Chrome(options=options_chrome) as browser:
    browser.get(url)
    song = browser.get_cookies()[0]['name']
    browser.find_element(By. ID, 'phraseInput').send_keys(song)
    browser.find_element(By.ID, 'checkButton').click()
    print(browser.find_element(By.ID, 'result').text)