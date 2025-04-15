# 🤖 Selenium-миссия: Раскрытие численности войск
#
# 🔹 Задача: Империя наносит ответный удар. Сосчитайте количество штурмовиков в армии Империи.
#
#     1️⃣ Зайдите на сайт-тренажёр с помощью Selenium.
#     2️⃣ Найдите все элементы с тегом <a>.
#     3️⃣ Пройдитесь по каждому элементу <a> и проверьте значение атрибута stormtrooper.
#     Суммируйте все числовые значения атрибута stormtrooper для получения общего количества штурмовиков.
#     4️⃣ Вставьте полученное значение всех штурмовиков на странице тренажера и нажмите кнопку "Проверить",
#     появится заветный пароль(в виде фразы), считайте его с помощью .text.
#     5️⃣ Вставьте пароль в поле ниже, между кавычками на Stepik.
#
# 💡 Совет: заведите переменную (счетчик) для подсчёта общего количества штурмовиков в армии.


from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.3.3/index.html')
    links = browser.find_elements(By.TAG_NAME, "a")
    sum_of_troopers = 0
    for i, val in enumerate(links):
        if val.get_attribute('stormtrooper').isdigit():
            sum_of_troopers += int(val.get_attribute('stormtrooper'))
    browser.find_element(By.ID, 'inputNumber').send_keys(sum_of_troopers)
    browser.find_element(By.ID, 'checkBtn').click()
    print(browser.find_element(By.ID, 'feedbackMessage').text)
    browser.quit()