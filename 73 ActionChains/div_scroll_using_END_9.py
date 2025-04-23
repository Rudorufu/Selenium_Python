# Применяем метод send_keys(Keys.END) для прокрутки содержимого контейнера.
#
# 🔹 Задача: прокрутить оба контейнера до конца и считать пароль.
#
#     1️⃣ Перейдите на сайт-тренажёр с помощью Selenium.
#     2️⃣Под каждым контейнером находится статусный блок, который изначально показывает «Статус: не прокручено».
#     С помощью ActionChains используя метод отправки клавиши END, прокрутить содержимое каждого контейнера до самого низа.
#     Как только содержимое контейнера прокручено до конца, соответствующий статусный блок должен обновиться: текст изменится на «Прокручено!»,
#     а фон изменится на зелёный (подсветка).
#     3️⃣После того как оба контейнера прокручены до конца, ниже появляется блок с секретным паролем.
#     Извлеките пароль из элемента, где он отображается (элемент имеет атрибут key="access_code").
#     4️⃣ Вставьте пароль здесь в поле ниже.
#
# 🟢 Внимание:
# Данный тренажёр работает только через Selenium – функционал появления пароля активен только если браузер запущен через WebDriver.
# 💡Подсказка
#
# Для того чтобы END сработал, сначала нужно взять контейнер в фокус, то есть кликнуть по нему:
#
# actions.click(container)...и далее цепочку с END


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import Keys
url = "https://parsinger.ru/selenium/7/7.3.5/index.html"


with webdriver.Chrome() as browser:
    browser.get(url)
    actions = ActionChains(browser)
    browser.find_element(By.ID, 'scrollable-container-left').click()
    actions.send_keys(Keys.END).perform()
    time.sleep(1)
    browser.find_element(By.ID, 'scrollable-container-right').click()
    actions.send_keys(Keys.END).perform()
    time.sleep(1)
    print(browser.find_element(By.CSS_SELECTOR, '[key="access_code"]').text)
