# Применим scroll_by_amount(x,y).
#
# Представьте ситуацию: вы открываете веб-страницу, но нужный элемент отсутствует в DOM-дереве.
# Единственный способ его загрузить — прокрутить страницу вниз, после чего элемент появится в DOM, и с ним можно будет взаимодействовать.
#
# 🔹 Задача:
#
#     1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Используя метод scroll_by_amount(x, y), прокрутите страницу вниз и считайте код, который появится спустя 3 секунды.
#     3️⃣ Прокрутите страницу ещё раз, введите полученный на предыдущем шаге код и нажмите кнопку «Проверить».
#     4️⃣ Если всё выполнено правильно, появится пароль. Вставьте этот пароль в поле ответа степик.
#
# 🟢 Внимание: данный тренажёр работает только через Selenium. Также разрешения могут отличаться — подберите правильный y под себя.
#
# 🔥 Пока работу с ожиданиями мы еще не прошли, поэтому работаем через time.sleep(). Кто уже знает, как работать с ожиданиями — welcome!


import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


url = 'https://parsinger.ru/selenium/7/7.4.1/index.html'

with webdriver.Chrome() as browser:
    browser.get(url)
    ActionChains(browser).scroll_by_amount(1, 500).perform()
    time.sleep(5)
    secret = browser.find_element(By.CLASS_NAME, 'countdown').text
    secret = secret.split()[1]
    time.sleep(1)
    div = browser.find_element(By.CLASS_NAME, 'step-container')
    ActionChains(browser).move_to_element(div).scroll_by_amount(1, 1500).perform()
    time.sleep(2)
    browser.find_element(By.TAG_NAME, 'input').send_keys(secret)
    browser.find_element(By.TAG_NAME, 'button').click()
    print(browser.find_element(By.ID, 'final-key').text)
