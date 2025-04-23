# Прокрутка страницы Keys.
#
# 🔹 Задача: с помощью Selenium заполните все поля и получите пароль.
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Заполните любым текстом каждое появляющееся поле. После ввода текста нажмите Enter, чтобы подтвердить заполнение поля.
#     3️⃣ После заполнения каждого поля нажмите ArrowDown, чтобы перейти к следующему полю. Новые поля будут появляться динамически.
#     4️⃣ Повторяйте процесс, пока не будет заполнено 100 полей.
#     5️⃣ После заполнения всех полей и подтверждения, пароль появится в элементе с id="hidden-password".
#     6️⃣ Извлеките текст пароля и вставьте его в поле ниже между кавычками.
#
# 💡 Совет: в данном задании можно обойтись без ActionChains. Ну и как обычно выводите пароль в print()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
url = "https://parsinger.ru/selenium/7/7.2/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    list_input = []
    i = 0
    while i != 100:
        input_tags = [x for x in browser.find_elements(By.CLASS_NAME, 'interactive')]
        for tag_input in input_tags:
            if tag_input not in list_input:
                tag_input.send_keys('text')
                tag_input.send_keys(Keys.ENTER)
                tag_input.send_keys(Keys.DOWN)
                time.sleep(.3)
                list_input.append(tag_input)
                i += 1
    print(browser.find_element(By.ID, 'hidden-password').text)