# 1️⃣ Зайдите на сайт-тренажер с помощью Selenium.
# 2️⃣ Нажмите кнопку "Начать миссию".
# 3️⃣ Получите пароль, который появится на экране (с помощью метода .text).
# 4️⃣ Введите этот пароль в поле и нажмите кнопку "Проверить".
# 5️⃣ Если пароль правильный, появится финальный ключ. Его нужно извлечь из элемента с id="text2". И вставить здесь в поле ниже между кавычек.


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.2.3/index.html')
    browser.find_element(By.ID, "showTextBtn").click()
    text = browser.find_element(By.ID, "text1").text
    browser.find_element(By.ID, 'userInput').send_keys(text)
    browser.find_element(By.ID, 'checkBtn').click()
    result = browser.find_element(By.ID, 'text2').text
    browser.quit()
    print(result)