#↔️ Применяем drag_and_drop_by_offset.
#
# 🔹 Задача: помогите Питеру Гриффину добраться до бассейна, термометр показывает +35🌡️.
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Перетащите мистера Гриффина в бассейн и получите пароль в виде фразы.
#     3️⃣ Извлеките текст пароля из появившегося элемента с id="password" и вставьте его в поле ниже между кавычками.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
url = "http://parsinger.ru/selenium/7/7.3.1/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    draggable = browser.find_element(By.ID, 'draggable')
    actions = ActionChains(browser)
    actions.drag_and_drop_by_offset(draggable, 0, -300).perform()
    print(browser.find_element(By.ID, 'password').text)