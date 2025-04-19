# ↕️ Прокрутка к элементу.
#
# 🔹 Задача: На сайте-тренажёре вам предстоит выполнить несколько шагов, связанных с прокруткой и взаимодействием с элементами.
#
#     1️⃣ Откройте сайт-тренажёр с помощью Selenium.
#     2️⃣ Прокрутите страницу вниз до кнопки "Финиш!". Используйте scrollIntoView()метод прокрутки к элементу с id="target".
#     3️⃣ Нажмите на кнопку "Финиш!".
#     4️⃣ Извлеките секретный ключ.
#     5️⃣ Вставьте пароль в поле ниже, между кавычками.
#
# 💡 Совет: выведите результат в print().


from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://parsinger.ru/selenium/6/6.5/index.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    element = browser.find_element(By.ID, 'target')
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    browser.find_element(By.ID, 'target').click()
    print(browser.find_element(By.ID, 'secret-key-container').text)