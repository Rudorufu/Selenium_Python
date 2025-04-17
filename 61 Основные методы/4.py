# 🔹 Задача: сделать скриншот
#
#     1️⃣ Зайти на сайт-тренажёр с помощью Selenium.
#     2️⃣ Найти картинку с id="this_pic"
#     3️⃣ Сделать скриншот картинки.
#     4️⃣ На ней будет код, который вам нужно будет ввести здесь в поле ниже.
#
# 💡 Совет: на сайте есть защита, если вы не используете Selenium.
# Можете добавить time.sleep("Много секунд") чтобы изучить тренажер.


from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/6/6.2.1/index.html') # Откройте сайт с помощью Selenium
    pic = browser.find_element(By.ID, 'this_pic').screenshot('D:\\scr.png')