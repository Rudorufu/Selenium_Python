# 🔲 Применяем window_handles.
#
# 🔹 Задача: Получить секретный ключ, суммируя числа, появляющиеся на 5 страницах, и вставить итог в поле на главной странице.
# Если вы все сделали правильно, система выдаст пароль.
#
#     1️⃣ С помощью Selenium запустите браузер и откройте главную страницу сайта-тренажера
#     2️⃣ На главной странице соберите 5 ссылок и откройте их в новых вкладках.
#
# 🟢Примечание: Главная страница доступна даже без Selenium, но для остальных страниц требуется управление через Selenium!
#
#     3️⃣ Спустя 3 сек, на каждой странице появится по 3 числа, соберите их и получите сумму всех чисел.
#     4️⃣ Вернитесь на главную страницу и вставьте полученное значение в поле и нажмите кнопку "Проверить"
#     5️⃣ Если вы все сделали правильно, система выдаст пароль. Считайте его и введите на степик в поле ниже между кавычками.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
url = "https://parsinger.ru/selenium/8/8.1.2/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    timer = browser.find_element(By.ID, 'timer').text
    elems = browser.find_elements(By.TAG_NAME, 'a')
    links = [elem.get_attribute('href') for elem in elems]
    for link in links:
        browser.switch_to.new_window('tab')
        browser.get(link)
    print('Timer:', timer)
    time.sleep(int(timer))
    nums_all = 0
    for i, link in enumerate(links):
        browser.switch_to.window(browser.window_handles[i + 1])
        nums = browser.find_elements(By.CLASS_NAME, 'number')
        for j in nums:
            nums_all += int(j.text)
        time.sleep(2)
    browser.switch_to.window(browser.window_handles[0])
    browser.find_element(By.ID, 'sumInput').send_keys(nums_all)
    browser.find_element(By.ID, 'checkButton').click()
    print('Sum of numbers:', nums_all)
    print(browser.find_element(By.ID, 'passwordDisplay').text)