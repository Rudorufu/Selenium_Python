# 🎨 Операция: Цветовая Синхронизация
#
# Здравствуйте, аспиранты автоматизации! Сегодня перед вами задача, которая перенесёт нас в мир цветов, чисел и быстрых решений.
# Вас ждёт настоящий квест на ловкость рук и точность кода. Сможете ли вы перенести данные так, чтобы они заиграли новыми красками?
# На этот раз задание не только проверит вашу скорость, но и научит работать с изменением стилей элементов на странице.
# Скорость и точность — вот ваши лучшие союзники в этой миссии!
# Задачи
#
#     Исследование Территории: Откройте веб-сайт с помощью Selenium. Проанализируйте поля, с которыми предстоит работать.
#
#     Миссия "Синхронизация": На странице находятся 100 текстовых полей: 50 серых и 50 синих. Ваша задача — перенести числа из серых полей в синие.
#
#
#     Проверка и Контроль: Нажмите на кнопку "Проверить". Если перенос чисел прошёл успешно, поля станут зелёными.
#
#     Получение Кода: Секретный код появится только в том случае, если все поля успешно стали зелёными. Секретный код нужно будет вставить в поле для ответа на Stepik.
#


from selenium import webdriver
from selenium.webdriver.common.by import By
url = 'https://parsinger.ru/selenium/5.5/4/1.html'


with webdriver.Chrome() as browser:
    browser.get(url)
    bloks = browser.find_elements(By.CLASS_NAME, 'parent')
    for element in bloks:
        value = element.find_element(By.XPATH, './textarea[1]').text
        element.find_element(By.XPATH, './textarea[1]').clear()
        element.find_element(By.XPATH, './textarea[2]').send_keys(value)
        element.find_element(By.XPATH, './button').click()
    browser.find_element(By.ID, 'checkAll').click()
    print(browser.find_element(By.ID, 'congrats').text)