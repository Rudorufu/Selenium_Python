# 🧹 Удалите все cookies.
#
# 🔹 Задача: удалите все печеньки🍪 на сайте-тренажере
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Удалить все cookies, появится пароль.
#     3️⃣ Вставить пароль в поле ниже, между кавычками.


url = 'https://parsinger.ru/selenium/6/6.3.2/index.html'
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('--headless')


with webdriver.Chrome(options=options_chrome) as browser:
    browser.get(url)
    browser.delete_all_cookies()
    time.sleep(1)
    print(browser.find_element(By.ID, 'password').text)